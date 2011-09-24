import os, random, struct, zmq

context = zmq.Context()
pusher = context.socket(zmq.PUSH)
seed = context.socket(zmq.PULL)
pusher.connect('tcp://192.168.1.123:5555')
seed.bind('tcp://192.168.1.123:5556')

while True:
    pusher.send(''.join(struct.pack('B', random.getrandbits(8)) for i in range(8192)))
    rnd = seed.recv()
    if rnd:
        random.seed(rnd)
