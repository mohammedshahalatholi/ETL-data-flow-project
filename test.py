
from decorator import comment
import time
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