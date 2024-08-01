import eventlet
import json
import os
import time
from flask import Flask, send_from_directory
from flask_socketio import SocketIO
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4

eventlet.monkey_patch()

def get_mp3_length(filename):
    try:
        audio = MP3(filename)
    except:
        audio = MP4(filename)
    return audio.info.length

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins=['http://untitlednam.tplinkdns.com:5173'], async_mode='eventlet')

def recursive_loopthru():
    for i in os.listdir('./music'):
        if i.endswith('.mp3'):
            iterator = 0
            print(f'Sending {i} to client')
            while iterator < round(get_mp3_length('./music/' + i)):
                socketio.emit('new_music', {'filename': i, 'length': get_mp3_length(f'./music/{i}'), 'timestamp': iterator})
                iterator += 1
                time.sleep(1)

    recursive_loopthru()

@app.route('/')
def index():
    return "<h1>hi there! this is a backend server so this is the only text which is also just for testing</h1>" \
            '<a href="http://untitlednam.tplinkdns.com:5173">Go back</a>'

@app.route('/jpgs/<filename>')
def send_image(filename):
    return send_from_directory('./jpgs', filename, mimetype='image/jpeg')

@app.route('/music/<filename>')
def send_music(filename):
    return send_from_directory('./music', filename)

@socketio.on('connect')
def connected():
    print('Client connected')

@socketio.on('disconnect')
def disconnected():
    print("User disconnected")

@socketio.on('chat message')
def handle_chat(msg):
    global latest_msg
    try:
        print(latest_msg)
        if latest_msg == msg:
            return
    except NameError:
        pass

    latest_msg = ""
    socketio.emit('chat message', msg)
    latest_msg = msg
    with open('./client/src/lol.json', "r") as f:
        global data
        data = json.load(f)
        print(data)
        data.append(msg)
        print(data)

    with open('./client/src/lol.json', "w") as f:
        json.dump(data, f)

if __name__ == '__main__':
    socketio.start_background_task(target=recursive_loopthru)
    socketio.run(app, host="0.0.0.0", port=3000)
