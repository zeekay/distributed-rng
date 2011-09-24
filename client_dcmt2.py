import dcmt, os, struct, zmq

context = zmq.Context()
pusher = context.socket(zmq.PUSH)
pusher.connect('tcp://192.168.1.123:5555')

mt = dcmt.DcmtRandom()

while True:
    pusher.send(struct.pack('B', mt.getrandbits(8)))
