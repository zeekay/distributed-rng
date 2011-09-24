import zmq

context = zmq.Context()
reciever = context.socket(zmq.PULL)
reciever.bind('tcp://127.0.0.1:5555')

while True:
    print reciever.recv()
