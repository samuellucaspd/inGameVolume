from flask import Flask, request, render_template,redirect
import webview
from core import get_programs
import requests
import threading
import start

profile_picture_url = None
process = None
app = Flask(__name__)
window = webview.create_window('InGameVolume', app)
programs = get_programs()
running = False
stt = start.Start()

vol = None
program = None
time = None


url = "https://api.github.com/users/samuellucaspd"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    profile_picture_url = data["avatar_url"]


@app.route('/')
def index():
    return render_template('index.html', programs=programs, len=len(programs), pic=profile_picture_url)

@app.route('/start', methods=['POST'])
def st():
    global vol
    global time
    global program
    vol = request.form.get('vol')
    vol = float(vol) / 100
    time = request.form.get('time')
    time = int(time)
    program = request.form.get('program')
    return render_template('running.html')

@app.route('/start_process',methods = ['GET'])
def start_process():
    print("acessado")
    global program
    global vol
    global time
    stt.running = True
    process = threading.Thread(target=stt.start(program,vol,time))
    process.start()
    return 'OK'

@app.route('/stop',methods = ['POST'])
def stop():
    stt.running = False
    return redirect('/')
if __name__ == '__main__':
    webview.start()