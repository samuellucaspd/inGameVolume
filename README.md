# inGameVolume
This repository contains a Python project to control the audio volume of specific programs while the user plays. The project uses the Flask, webview and pycaw libraries to create a web interface and control the audio volume.

The app.py file contains the main code for the Flask application. It defines routes for rendering HTML templates, displaying available programs, and starting or stopping volume control. The app also makes a GitHub API call to get the URL of the user's profile picture.

The core.py file contains a helper function that uses the pycaw library to obtain a list of running programs, which will be displayed in the interface.

The start.py file runs as a separate process and is responsible for starting the volume control for the selected program. It reads settings from settings.ini file, gets program name, volume and control time. It then uses the pycaw library to adjust the volume of the selected program. When a specific key is pressed, the volume is restored to normal.

The project has a settings.ini file that stores user settings such as volume, program and time control.

This repository can be cloned and run locally to control the audio volume of specific programs during gameplay.
