
# from socket import socket
from flask import Flask
from flask_socketio import SocketIO
import random
from time import sleep
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, cors_allowed_origins="*")
socketio = SocketIO(app, cors_allowed_origins='*')

thread_flowcoord = None

def process():
    data=[]
    for _ in range(7):
        data.append(round(random.random(),2))
    return data

def get_rank():
    data=[]
    for i in range(16):
        data.append({
            "count":round(random.random(),2),
            "flow":"src:xxx     dest:xxx    {0}".format(i)
        })
    return data


def update_flow_coord():
    while True:
        socketio.sleep(1)
        result=get_rank()
        socketio.emit('updateTable',{'rank':result})

@socketio.on('connect')
def handle_message():
    print("连接成功！！！")
    global thread_flowcoord
    if not thread_flowcoord:
        thread_flowcoord = socketio.start_background_task(
            target=update_flow_coord)

if __name__ == '__main__':
    socketio.run(app, debug=True, host="127.0.0.1", port=10020)
