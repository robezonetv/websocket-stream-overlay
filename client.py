#!/usr/bin/python3

import socketio
import sys

# standard Python
sio = socketio.Client()

sio.connect('http://127.0.0.1:5000/')

sio.emit('my_broadcast_event', {'data': sys.argv[1]})

sio.disconnect()
