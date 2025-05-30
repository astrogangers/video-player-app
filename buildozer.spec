[app]

# (str) Title of your application
title = Video Player

# (str) Package name
package.name = videoplayer

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
p4a.local_recipes =

# (str) Filename to the hook for p4a
p4a.hook =

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
p4a.port =

# (str) xml file to include as an intent filters in <activity> tag
android.manifest.intent_filters =

# (str) Activity to start (only with android.private_storage = True)
android.activity_class = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
android.activity_class_name = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Python Service
android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
android.theme = @android:style/Theme.NoTitleBar

# (list) Pattern to whitelist for the whole project
android.whitelist =

# (str) Path to a custom whitelist file
android.whitelist_src =

# (str) Path to a custom blacklist file
android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
android.add_jars = 

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
android.add_java_files =

# (str) python-for-android branch to use, defaults to master
p4a.branch = master

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
android.manifest.intent_filters =

# (str) launchMode to set for the main activity
android.manifest.launch_mode = standard

# (list) Android additionnal libraries to copy into libs/armeabi
android.add_libs_armeabi = 

# (list) Android additionnal libraries to copy into libs/armeabi-v7a
android.add_libs_armeabi_v7a = 

# (list) Android additionnal libraries to copy into libs/arm64-v8a
android.add_libs_arm64_v8a = 

# (list) Android additionnal libraries to copy into libs/x86
android.add_libs_x86 = 

# (list) Android additionnal libraries to copy into libs/mips
android.add_libs_mips = 

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (via a string)
# Usage example : android.manifest_placeholders = key:value, key2:value2
android.manifest_placeholders =

# (bool) Skip byte compile for .py files
android.no-byte-compile-python = False

# (str) Use a specific python version (cross-compilation only)
python.version = 3.9

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
bin_dir = ./bin
