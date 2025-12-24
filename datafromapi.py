import requests
import json
from grnrator import comment
response=requests.get("http://127.0.0.1:8000/")

data=response.json()

#print("its from api",data)

# def chekdup(*dat):
#     print(dat)
    
# chekdup(data)
@comment
def dupcheck(data):
    datacpy=data.copy()
    out=[]
    count=0
#print(datacpy)

    while datacpy:
        dupcount=0
        for x in datacpy:
            if x not in out:
                out.append(x)
        datacpy.remove(x)

    print(out)