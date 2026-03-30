# Spotilike 🎵

## Like your current Spotify song with a single keystroke—no windows, no interruptions.

---

### 🛠️The Problem

As a power user and multitasker, I found it disruptive to Alt-Tab out of a focused session (gaming, working, or browsing the internet) just to "Like" a song on Spotify. Most media keys handle Play/Pause, but "Liking" requires manual interaction with the UI.

---

### 💡 The Solution

Spotilike is a lightweight Python integration that maps a physical macro key to Spotify's 'Library-Modify' API. It runs 100% invisibly in the background with zero terminal flashes or window pop-ups.

### 🚀 Technical Features

- OAuth2 Authentication: Securely handles user authorization via the Spotipy library.

- Headless Execution: Compiled into a standalone .exe using PyInstaller with the --noconsole flag.

- Dynamic Pathing: Smart directory handling ensures the .cache token is found regardless of where the script is launched from.

- Hardware Bridge: Uses an AutoHotkey (v2) to trigger the Python backend silently.

### 📦 Prerequisites

- **Windows 10/11**

- **AutoHotkey v2.0+: Required to run the .ahk bridge that listens for the macro keys.**

- **Python 3+**

(Mac OS:apple: and Linux:penguin: versions coming soon!)

---

## 📦 Installation & Setup

1. Clone the Repo

   ```
   git clone https://github.com/sbescobar/Spotilike.git

   ```

2. Spotify Credentials: Create an app on the Spotify Developer Dashboard (https://developer.spotify.com/) and get your CLIENT_ID and CLIENT_SECRET from.

3. Environment Setup: Add your credentials to the src/Spotilike.py file.

4. Install dependencies: pip install spotipy pyinstaller.

5. Build the EXE: python -m PyInstaller --onefile --noconsole Spotilike.py

## 🚀 Quick Start Guide

**Step 1: Create your Spotify "App"**

**(IMPORTANT YOU NEED A PREMIUM SPOTIFY ACCOUNT TO MAKE APPS)**

Go to the Spotify Developer Dashboard (https://developer.spotify.com/).
Create a developer account

    Click Create App.

        App Name: Spotilike

        Set Redirect URL: http://127.0.0.1:8000/callback (Required for the handshake).

    Save and copy your Client ID and Client Secret.

**Step 2: Configure & Build**

    Clone this repository or download the files.

    Open Spotilike.py in a text editor and paste your credentials into the CLIENT_ID and CLIENT_SECRET fields.

    Run the provided setup_spotilike.bat file. This will automatically:

        Install necessary libraries (spotipy, pyinstaller).

        Build your personalized, secure Spotilike.exe in the /dist folder.

**Step 3: The One-Time "Handshake"**

    Run the new Spotilike.exe from your /dist folder.

    A browser window will open—log in and click Agree.

    Once you see "Success," close the browser. A .cache file will appear in your folder. Do not delete this—it is your permanent "passport" for silent liking.

**Step 4: Map your Folder**

    In Spotilike_hotkey.ahk: Update the SpotifyScriptPath variable to point to your /dist folder.

    Run the AHK script. Play a unliked song, hit your macro key, and watch the + symbol turn into a checkmark fill on Spotify!

## 🛡️ Security Note

This project uses OAuth2. Your personal CLIENT_SECRET and .cache tokens should **NEVER** be shared. A .gitignore is included to prevent accidental leaks.

---

## :heavy_check_mark: Pro-Tip: To make it "Always On"

### To ensure your hotkey works every time you turn on your PC:

Step 1: Press Win + R, type shell:startup, and hit Enter.

Step 2: Right-click your Spotilike.ahk file and select Create Shortcut.

Step 3: Move that Shortcut into the Startup folder you just opened.

Now, the bridge will load automatically when Windows starts!
