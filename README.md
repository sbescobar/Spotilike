# Spotilike 🎵
Like your current Spotify song with a single keystroke—no windows, no interruptions.

## 🛠️ The Problem
As a power user and multitasker, I found it disruptive to Alt-Tab out of a focused session (gaming, working, or browsing the internet) just to "Like" a song on Spotify. Most media keys handle Play/Pause, but "Liking" requires manual interaction with the UI.

## 💡 The Solution
Spotilike is a lightweight desktop application that maps a universal hotkey to Spotify's 'Library-Modify' API. It runs invisibly in your system tray and provides a beautiful, custom-built borderless notification with the album art when you like a song!

## 🚀 Technical Features
- **Plug-and-Play Authentication**: Uses the Spotify PKCE (Proof Key for Code Exchange) flow. No complicated Developer portals or Client Secrets required for end-users!
- **Cross-Platform**: Natively supports both Windows and macOS with OS-specific hotkeys and notification placements.
- **Custom UI Overlays**: Uses a borderless, dark-themed Tkinter notification window that seamlessly fades out and fetches high-res album art directly from the API.
- **Headless System Tray**: Runs silently in the background via `pystray` and `pynput`, completely replacing the need for clunky AutoHotkey scripts.

##‼️Requirements‼️
Spotilike requires a Spotify Premium Subscription.

## 📦 Installation & Setup
1. Download the latest release `.zip` for Windows or Mac.
2. Extract the file and run `Spotilike.exe` (Windows) or `Spotilike-mac.app` (Mac).
3. The very first time you press the hotkey (`Ctrl + Alt + L`), your default web browser will open. Log into Spotify and click **Agree**.
4. You're done! A secure `.cache` token is saved automatically in your `AppData` (Windows) or `Library` (Mac) folder for seamless future use.

## ⌨️ How to Use
Make sure Spotify is playing a song in the background, then simply press:
- **Windows**: `Ctrl + Alt + L`
- **Mac**: `Cmd + Option + L`

A sleek popup will instantly appear in the corner of your screen showing the album art, track name, and artist to confirm the song was added to your Liked Songs!

## ✔️ Pro-Tip: "Always On" (Windows)
To ensure your hotkey works every time you turn on your PC:
1. Press `Win + R`, type `shell:startup`, and hit Enter.
2. Right-click your `Spotilike.exe` file and select **Create Shortcut**.
3. Move that Shortcut into the Startup folder you just opened.

Now, Spotilike will load silently in your system tray every time Windows starts!
