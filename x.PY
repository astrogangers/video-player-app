from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.video import Video
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
import json
import os

class VideoApp(App):
    def build(self):
        self.video_list = []
        self.load_playlist()
        self.user_seeking = False

        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.video = Video(source="", state='stop', options={'eos': 'stop'})
        self.video.size_hint_y = 0.4
        self.video.bind(position=self.update_slider)
        self.layout.add_widget(self.video)

        progress_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30, spacing=10)
        self.current_time_label = Label(text="00:00", size_hint_x=None, width=50)
        self.slider = Slider(min=0, max=1, value=0, cursor_size=(10, 10), background_width=2)
        self.slider.bind(on_touch_up=self.seek_video)
        self.total_time_label = Label(text="00:00", size_hint_x=None, width=50)
        progress_layout.add_widget(self.current_time_label)
        progress_layout.add_widget(self.slider)
        progress_layout.add_widget(self.total_time_label)
        self.layout.add_widget(progress_layout)

        controls_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        self.rewind_btn = Button(text="⏪ 10s")
        self.rewind_btn.bind(on_release=self.rewind_10s)
        self.play_pause_btn = Button(text="▶")
        self.play_pause_btn.bind(on_release=self.toggle_play_pause)
        self.forward_btn = Button(text="⏩ 10s")
        self.forward_btn.bind(on_release=self.forward_10s)
        controls_layout.add_widget(self.rewind_btn)
        controls_layout.add_widget(self.play_pause_btn)
        controls_layout.add_widget(self.forward_btn)
        self.layout.add_widget(controls_layout)

        self.url_input = TextInput(hint_text='أدخل رابط الفيديو ثم اضغط Enter', multiline=False, size_hint_y=None, height=40)
        self.url_input.bind(on_text_validate=self.add_video_url)
        self.layout.add_widget(self.url_input)

        open_btn = Button(text="اختر فيديو من الجهاز", size_hint_y=None, height=40)
        open_btn.bind(on_release=self.open_file_chooser)
        self.layout.add_widget(open_btn)

        self.scroll = ScrollView(size_hint_y=0.5)
        self.playlist_layout = GridLayout(cols=1, size_hint_y=None, spacing=5)
        self.playlist_layout.bind(minimum_height=self.playlist_layout.setter('height'))
        self.scroll.add_widget(self.playlist_layout)
        self.layout.add_widget(self.scroll)

        self.refresh_playlist_ui()
        Clock.schedule_interval(self.refresh_slider_max, 0.5)

        return self.layout

    def add_video_url(self, instance):
        url = self.url_input.text.strip()
        if url:
            self.video_list.append(url)
            self.save_playlist()
            self.refresh_playlist_ui()
            self.url_input.text = ''
            self.play_video(url)

    def add_video_path(self, path):
        self.video_list.append(path)
        self.save_playlist()
        self.refresh_playlist_ui()
        self.play_video(path)

    def refresh_playlist_ui(self):
        self.playlist_layout.clear_widgets()
        for path in self.video_list:
            btn = Button(text=path, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.play_video(btn.text))
            self.playlist_layout.add_widget(btn)

    def play_video(self, path):
        self.video.source = path
        self.video.state = 'play'
        self.play_pause_btn.text = "⏸"

    def open_file_chooser(self, instance):
        box = BoxLayout(orientation='vertical')
        chooser = FileChooserListView()
        select_btn = Button(text="اختر هذا الملف", size_hint_y=None, height=40)

        popup = Popup(title="اختر فيديو", content=box, size_hint=(0.9, 0.9))
        box.add_widget(chooser)
        box.add_widget(select_btn)

        def confirm_selection(instance):
            if chooser.selection:
                self.add_video_path(chooser.selection[0])
                popup.dismiss()

        select_btn.bind(on_release=confirm_selection)
        popup.open()

    def save_playlist(self):
        try:
            with open("playlist.json", "w", encoding="utf-8") as f:
                json.dump(self.video_list, f)
        except:
            pass

    def load_playlist(self):
        try:
            if os.path.exists("playlist.json"):
                with open("playlist.json", "r", encoding="utf-8") as f:
                    self.video_list = json.load(f)
        except:
            self.video_list = []

    def refresh_slider_max(self, dt):
        if self.video.duration > 0:
            self.slider.max = self.video.duration
            self.total_time_label.text = self.format_time(self.video.duration)

    def update_slider(self, instance, value):
        if not self.user_seeking:
            self.slider.value = value
            self.current_time_label.text = self.format_time(value)

    def seek_video(self, instance, touch):
        if instance.collide_point(*touch.pos) and self.video.duration > 0:
            self.user_seeking = True
            seek_percent = self.slider.value / self.video.duration
            self.video.seek(seek_percent)
            self.user_seeking = False

    def format_time(self, seconds):
        try:
            seconds = int(seconds)
            mins = seconds // 60
            secs = seconds % 60
            return f"{mins:02}:{secs:02}"
        except:
            return "00:00"

    def toggle_play_pause(self, instance):
        if self.video.state == 'play':
            self.video.state = 'pause'
            self.play_pause_btn.text = "▶"
        else:
            self.video.state = 'play'
            self.play_pause_btn.text = "⏸"

    def rewind_10s(self, instance):
        pos = max(0, self.video.position - 10)
        self.video.seek(pos / self.video.duration)

    def forward_10s(self, instance):
        pos = min(self.video.duration, self.video.position + 10)
        self.video.seek(pos / self.video.duration)

if __name__ == '__main__':
    VideoApp().run()
