
from decorator import comment
import time
def num():
    print("one")
    time.sleep(1)
#without using @ key
nums=comment(num)
#nums()

#with using decorator
@comment
def num2():
    print("Two")
    time.sleep(1)

#num2()



def argsdat(*data,**ddata):
    print(data)
    for x in data:
        print(x)
    print(ddata)
    for k,y in ddata.items():
        print(k,y)


argsdat("CS",34,343,name="same")

argsdat("ec",age=45,name="abc")