import sys
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# --- CONFIGURATION ---
# Get these from the Spotify Developer Dashboard: https://developer.spotify.com/dashboard
CLIENT_ID = 'YOUR_CLIENT_ID_HERE'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET_HERE'
REDIRECT_URI = 'http://127.0.0.1:8000/callback'
SCOPE = "user-library-modify user-read-currently-playing"

# --- DYNAMIC PATH HANDLING ---
# Ensures the .cache file is found relative to the EXE location, 
# preventing pathing errors when launched via iCUE/Task Scheduler.
if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

cache_path = os.path.join(script_dir, ".cache")

def like_current_song():
    """Fetches the currently playing Spotify track and adds it to Liked Songs."""
    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        cache_path=cache_path,
        open_browser=False  # Set to False for headless background execution
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)

    try:
        current_track = sp.currently_playing()
        
        if current_track and current_track['is_playing']:
            track_id = current_track['item']['id']
            track_name = current_track['item']['name']
            
            sp.current_user_saved_tracks_add(tracks=[track_id])
            print(f"Successfully Liked: {track_name}")
        else:
            print("No active playback detected.")
            
    except Exception as e:
        # Fallback: If token is expired or invalid, prompt for re-auth
        print(f"Authentication Error: {e}")
        auth_manager.open_browser = True
        auth_manager.get_access_token(as_dict=False)

if __name__ == "__main__":
    like_current_song()
