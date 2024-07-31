import json
import flask
import flask_socketio
import sys
import time

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app, cors_allowed_origins=['http://untitlednam.tplinkdns.com:5173'])

# Remove the global declaration for latest_msg
# global latest_msg
# latest_msg = ""

@app.route('/')
def index():
    return "<h1>hi there! this is a backend server so this is the only text which is also just for testing</h1>"

@socketio.on('connect')
def connected(s):
    print(s)
    print('connected')

@socketio.on('disconnect')
def disconnected():
    print("User disconnected")

@socketio.on('chat message')
def handle_chat(msg):
    global latest_msg  # Declare latest_msg as a global variable inside the function
    try:
        print(latest_msg)
        if latest_msg == msg:
            return
    except:
        # try harder
        pass
    latest_msg = ""  # Initialize latest_msg before using it
    socketio.emit('chat message', msg)
    latest_msg = msg  # Assign the new message to latest_msg
    with open('./client/src/lol.json', "r") as f:
        global data
        data = json.load(f)
        print(data)
        data.append(msg)
        print(data)

    with open('./client/src/lol.json', "w") as f:
        json.dump(data, f)

if __name__ == '__main__':
    socketio.run(app=app, host="0.0.0.0", port=3000, debug=True)