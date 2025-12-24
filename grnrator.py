import time

def comment(num):
    def dec(*data):
        print("program started")
        stated=time.time()
        num()
        ended=time.time()

        print("program ended")
        print("Programme ended within",ended-stated)
    return dec

def num():
    print("one")
    time.sleep(1)
#without using @ key
nums=comment(num)
nums()

#with using decorator
@comment
def num2():
    print("Two")
    time.sleep(1)

num2()


