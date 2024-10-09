from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

clients = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    clients.append(data['username'])
    print("User joined:", data)

@socketio.on('offer')
def handle_offer(data):
    socketio.emit('offer', data, broadcast=True)

@socketio.on('answer')
def handle_answer(data):
    socketio.emit('answer', data, broadcast=True)

@socketio.on('candidate')
def handle_candidate(data):
    socketio.emit('candidate', data, broadcast=True)

@socketio.on('screen-share')
def handle_screen_share(data):
    socketio.emit('screen-share', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
