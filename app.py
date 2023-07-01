from flask import Flask, request, render_template,redirect
import webview
from core import get_programs
import requests
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import pythoncom
import keyboard
import time
import subprocess
import configparser
profile_picture_url = None
process = None
config = configparser.ConfigParser()
config.read('./settings.ini')

url = "https://api.github.com/users/samuellucaspd"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    profile_picture_url = data["avatar_url"]

app = Flask(__name__)
window = webview.create_window('InGameVolume', app)
programs = get_programs()

@app.route('/')
def get_name():
    return render_template('index.html', programs=programs, len=len(programs), pic=profile_picture_url)



@app.route('/start', methods=['POST'])
def st():
    global process
    vol = request.form.get('vol')
    vol = float(vol) / 100
    time = request.form.get('time')
    time = int(time)
    program = request.form.get('program')
    print(program)
    config.set('settings','vol',str(vol))
    config.set('settings','program',program)
    config.set('settings','time',str(time))
    with open('settings.ini', 'w') as arquivo:
        config.write(arquivo)

    process = subprocess.Popen(['python', './start.py'])
    return render_template('running.html')
@app.route('/stop',methods = ['POST'])
def stop():
    process.terminate()
    return redirect('/')
if __name__ == '__main__':
    webview.start()