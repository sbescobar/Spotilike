#Requires AutoHotkey v2.0

; --- CONFIGURATION ---
; Change this to the folder where your Spotilike.exe is saved
SpotifyScriptPath := "full file path where your Spotilike.exe is saved"
ExecutableName := "SpotiLike.exe"

; --- HOTKEY ---
; Press Ctrl + Alt + L to like the song
^!l::
{
    ; Joins the folder path and exe name together
    FullTarget := SpotifyScriptPath . "\" . ExecutableName
    
    ; "Hide" ensures no window or black box pops up
    Run(FullTarget, SpotifyScriptPath, "Hide")
}
