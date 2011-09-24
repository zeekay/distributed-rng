import dcmt, os, zmq

context = zmq.Context()
pusher = context.socket(zmq.PUSH)
pusher.connect('tcp://192.168.1.123:5555')

while True:
    mt = dcmt.DcmtRandomState.range(1)[0]
    for i in range(100):
        data = ''
        for i in range(32):
            arr = mt.rand(1024)
            data += arr.tostring()
            del arr
        pusher.send(data)
    del mt
