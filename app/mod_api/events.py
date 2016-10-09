from flask_socketio import send, emit
from flask import request
from app import socketio
from app.mod_api.model import EClass


@socketio.on("connection", namespace="/api")
def handle_connection():
    emit("message", "hello")


@socketio.on("pressed", namespace="/api")
def handle_pressed():
    emit('message', {"data": "hello"})
    print("key pressed")


@socketio.on('disconnect', namespace='/api')
def test_disconnect():
    print('Client disconnected', request.sid)
