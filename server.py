#!/usr/bin/python3

async_mode = None

from flask import Flask, render_template
import socketio

sio = socketio.Server(logger=True, async_mode=async_mode)
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)
app.config['SECRET_KEY'] = 'secret!'
thread = None


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        sio.sleep(10)
        count += 1
        sio.emit('my_response', {'data': 'Server generated event'})

@app.route('/')
def index():
    #global thread
    #if thread is None:
    #    thread = sio.start_background_task(background_thread)
    return render_template('index.html')

@sio.event
def my_broadcast_event(sid, message):
    sio.emit('my_response', {'data': message['data']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
