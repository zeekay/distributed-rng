#!/usr/bin/env python
import os, zmq

context = zmq.Context()
pusher = context.socket(zmq.PUSH)
pusher.connect('tcp://192.168.1.123:5555')

packet_size = 8192

while True:
    pusher.send(os.urandom(packet_size))
