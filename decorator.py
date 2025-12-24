import time

def comment(fun):
    def dec(*args, **kwargs):
        print("program started")
        started = time.time()
        fun(*args, **kwargs)
        ended = time.time()
        print("program ended")
        print("Programme ended within", ended - started)
    return dec
