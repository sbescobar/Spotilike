import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyPKCE
from pathlib import Path
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw, ImageTk
from pynput import keyboard
import threading
import subprocess
import urllib.request
import io
import tkinter as tk

# --- DEVELOPER CONFIGURATION ---
CLIENT_ID = "1302ec399b644676a81b46eb8ea093a1"
# -------------------------------

def get_app_data_folder():
    """ Locates C:/Users/<User>/AppData/Roaming/Spotilike """
    app_data_path = Path(os.getenv('APPDATA')) / "Spotilike"
    if not app_data_path.exists():
        app_data_path.mkdir(parents=True, exist_ok=True)
    return app_data_path

CACHE_PATH = get_app_data_folder() / ".cache"
global_icon = None

def create_image(width, height, color1, color2):
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    dc = ImageDraw.Draw(image)
    dc.ellipse(
        (0, 0, width, height),
        fill=color1,
        outline=color2)
    return image

def show_custom_notification(title, artist, image_url):
    root = tk.Tk()
    root.overrideredirect(True) 
    root.configure(bg='#080808')
    root.attributes('-topmost', True)
    
    photo = None
    if image_url:
        try:
            req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as url:
                raw_data = url.read()
            im = Image.open(io.BytesIO(raw_data))
            im = im.resize((64, 64), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(im)
        except Exception:
            pass

    frame = tk.Frame(root, bg='#080808', padx=12, pady=12)
    frame.pack(fill=tk.BOTH, expand=True)
    
    if photo:
        img_label = tk.Label(frame, image=photo, bg='#080808')
        img_label.image = photo # Keep reference
        img_label.pack(side=tk.LEFT, padx=(0, 15))
        
    text_frame = tk.Frame(frame, bg='#080808')
    text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    title_label = tk.Label(text_frame, text=title, font=("Segoe UI", 12, "bold"), fg="#FFFFFF", bg="#080808", anchor="w")
    title_label.pack(side=tk.TOP, fill=tk.X)
    
    artist_label = tk.Label(text_frame, text=artist, font=("Segoe UI", 10), fg="#B3B3B3", bg="#080808", anchor="w")
    artist_label.pack(side=tk.TOP, fill=tk.X)
    
    root.update_idletasks()
    width = 380
    height = 88
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = screen_width - width - 24 
    y = screen_height - height - 60
    
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    def fade_out():
        alpha = root.attributes("-alpha")
        if alpha > 0:
            alpha -= 0.05
            root.attributes("-alpha", alpha)
            root.after(30, fade_out)
        else:
            root.destroy()
            
    root.after(3500, fade_out)
    root.mainloop()

def like_current_song():
    if CLIENT_ID == "YOUR_CLIENT_ID_HERE" or not CLIENT_ID:
        if global_icon:
            global_icon.notify("Developer hasn't set the Client ID in the script.", "Spotilike Setup Required")
        return
        
    scope = "user-library-modify,user-read-currently-playing"
    sp_oauth = SpotifyPKCE(
        client_id=CLIENT_ID,
        redirect_uri="http://127.0.0.1:8000/callback",
        scope=scope,
        cache_path=str(CACHE_PATH)
    )

    try:
        sp = spotipy.Spotify(auth_manager=sp_oauth)
        current_track = sp.current_user_playing_track()
        
        if current_track and current_track['item']:
            track_id = current_track['item']['id']
            track_name = current_track['item']['name']
            artist_name = current_track['item']['artists'][0]['name']
            
            image_url = ""
            try:
                # Get the 300x300 image if available
                image_url = current_track['item']['album']['images'][1]['url'] 
            except (IndexError, KeyError):
                try:
                    image_url = current_track['item']['album']['images'][0]['url']
                except:
                    pass

            # Add to liked songs
            sp.current_user_saved_tracks_add(tracks=[track_id])
            
            # Launch the custom UI notification!
            if getattr(sys, 'frozen', False):
                subprocess.Popen([sys.executable, "--notify", track_name, artist_name, image_url])
            else:
                subprocess.Popen([sys.executable, __file__, "--notify", track_name, artist_name, image_url])
                
        else:
            if global_icon:
                global_icon.notify("No song is currently playing.", "Spotilike")
    except Exception as e:
        if global_icon:
            global_icon.notify(f"Error: {e}", "Spotilike Error")

def on_hotkey():
    # Run the like action in a separate thread so it doesn't block the hotkey listener
    threading.Thread(target=like_current_song, daemon=True).start()

def setup_hotkeys():
    # hotkey listener using pynput
    hotkey = '<ctrl>+<alt>+l'
    listener = keyboard.GlobalHotKeys({
        hotkey: on_hotkey
    })
    listener.start()
    return listener

def on_quit(icon, item):
    icon.stop()

def main():
    # Check if this process was spawned just to show a notification
    if len(sys.argv) >= 5 and sys.argv[1] == "--notify":
        show_custom_notification(sys.argv[2], sys.argv[3], sys.argv[4])
        return

    global global_icon
    
    image = create_image(64, 64, '#1DB954', 'white')
    
    # Setup tray menu
    menu = pystray.Menu(
        item('Quit', on_quit)
    )
    
    # Create the tray icon
    global_icon = pystray.Icon("Spotilike", image, "Spotilike", menu)
    # Start the hotkey listener in the background
    listener = setup_hotkeys()
    global_icon.run()
    listener.stop()

if __name__ == "__main__":
    main()
