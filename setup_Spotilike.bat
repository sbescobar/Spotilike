@echo off
title Spotilike Builder
echo ----------------------------------------------------
echo Checking for Python dependencies...
pip install spotipy pyinstaller
echo ----------------------------------------------------
echo.
echo Building your personalized Spotilike.exe...
echo This may take a minute...
echo.
python -m PyInstaller --onefile --noconsole Spotilike.py
echo.
echo ----------------------------------------------------
echo SUCCESS! Your invisible EXE is now in the "dist" folder.
echo You can now close this window.
pause
