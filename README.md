# SpotiLike
Like current song played on your Spotify with keystroke.
---

🛠️ #The Problem
As a power user and multitasker, I found it disruptive to Alt-Tab out of a focused session (gaming, working, or browsing the internet) just to "Like" a song on Spotify. Most media keys handle Play/Pause, but "Liking" requires manual interaction with the UI.
---
💡 # The Solution

  Spotilike is a lightweight Python integration that maps a physical macro key to Spotify's 'Library-Modify' API. It runs 100% invisibly in the background with zero terminal flashes or window pop-ups.
---
🚀 #Technical Features

  OAuth2 Authentication: Securely handles user authorization via the Spotipy library.

  Headless Execution: Compiled into a standalone .exe using PyInstaller with the --noconsole flag.

  Dynamic Pathing: Smart directory handling ensures the .cache token is found regardless of where the script is launched from.

  Hardware Bridge: Uses an AutoHotkey (v2) to trigger the Python backend silently.
---
📦 # Prerequisites
  Windows 10/11: The compiled version is built for Windows.

  AutoHotkey v2.0+: Required to run the .ahk bridge that listens for the macro keys.
  
  Python 3.8+: Installed on your system.
  Pip Libraries: You will need to install the following dependencies: pip install spotipy python-dotenv pyinstaller
---
📦 # Installation & Setup

  1. Clone the Repo:

    git clone https://github.com/sbescobar/Spotilike.git

  2.  Spotify Credentials: Create an app on the Spotify Developer Dashboard and get your CLIENT_ID and CLIENT_SECRET.

  3. Environment Setup: * Add your credentials to the src/Spotilike.py file.

  Install dependencies: pip install spotipy pyinstaller.

  Build the EXE: python -m PyInstaller --onefile --noconsole Spotilike.py
---
🛡️ #Security Note

This project uses OAuth2. Your personal CLIENT_SECRET and .cache tokens should never be committed to a public repository. A .gitignore is included to prevent accidental leaks.
---

This "Quick Start" guide is perfect for your README because it breaks the process down into bite-sized, logical steps. It transitions from the "Web Setup" (Spotify) to the "Local Setup" (Files) and finally the "Hardware Setup" (iCUE).
🚀 Quick Start Guide

Follow these steps to get Spotilike running on your machine in under 5 minutes.

#Step 1: Create your Spotify "App"

Before running the code, you need your own API keys from Spotify.

  Go to the Spotify Developer Dashboard. (https://developer.spotify.com/dashboard) 

  Log in and click Create App.

  App Name: Spotilike (or anything you prefer).

  Redirect URI: You MUST add http://127.0.0.1:8000/callback to the Redirect URIs field in settings.

  Save and copy your Client ID and Client Secret.

#Step 2: Configure the Script

  Download the Spotilike.py file from the /src folder.

  Open the file in any text editor (Notepad, VS Code, etc.).

  Paste your Client ID and Client Secret into the designated variables at the top of the script.

  (Optional) If you are using the pre-compiled .exe, ensure it is in the same folder as your .ahk script.

#Step 3: The One-Time "Handshake"

  Double-click Spotilike.exe (or run the .py script manually).

  A browser window will automatically open asking you to log in to Spotify and "Agree" to the permissions.

  Once you see the "Success" message in your browser, close it.

  A file named .cache will appear in your folder. Do not delete this—it is your "passport" that allows the script to run silently in the future.

#(OPTIONAL)Step 4: Map your Hardware (iCUE Users)

To make your G-key trigger the script invisibly:

  In iCUE: Assign any of the macro keys to a "Keyboard Key" and select F13.

  In AutoHotkey: Run the Spotilike.ahk script.

  Test it: Play a song on Spotify and hit G3. If the song appears in your "Liked Songs" without a window popping up, you’re all set!

---
  🛡️ Pro-Tip: Make it "Always On"

To ensure your G3 key works every time you turn on your PC:

  Press Win + R, type shell:startup, and hit Enter.

  Right-click your Spotilike.ahk file and select Create Shortcut.

  Move that Shortcut into the Startup folder you just opened.

  Now, the bridge will load automatically when Windows starts!
