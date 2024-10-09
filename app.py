from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# WebRTC signaling
@socketio.on('offer')
def handle_offer(offer):
    socketio.emit('offer', offer, broadcast=True)

@socketio.on('answer')
def handle_answer(answer):
    socketio.emit('answer', answer, broadcast=True)

@socketio.on('ice-candidate')
def handle_ice_candidate(candidate):
    socketio.emit('ice-candidate', candidate, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
