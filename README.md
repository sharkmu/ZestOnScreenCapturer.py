# ZestOnScreenCapturer
Dynamic python on-screen app recording solution, Zest records on screen apps in proper fps, and automatically resizes to the size of the window selected with a sampling rate of 1 second.
# Usage
```py
from zest import capture_and_display
# Call the function with the desired window title
capture_and_display('BlueStacks App Player')
# Press 'q' to quit
```
This app was created when I wanted to create an AI model that plays a game on BlueStacks (Android Emulator for using Android apps on PC), and I faced the problem of not being able to get a decent fps with the existing libraries I found.
<br>
<br>
Right now the app outputs the input recorded video in real time, and the current implementation of zest.py can be modified to use the video stream in any python app.
<br><br>
**Note:** The app needs to be visible on screen for Zest to be able to work.
