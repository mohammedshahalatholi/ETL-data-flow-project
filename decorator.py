import time

def comment(fun):
    def dec():
        print("program started")
        stated=time.time()
        fun()
        ended=time.time()

        print("program ended")
        print("Programme ended within",ended-stated)
    return dec




