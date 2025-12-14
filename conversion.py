from datas import listdata

# n=len(listdata)

# out=[]
# for x in range(n):
#     for y in range(n-1):
#         if listdata[y]>listdata[y+1]:
#             listdata[y],listdata[y+1]=listdata[y+1],listdata[y]


# for val in listdata:
#     if val not in out:
#         out.append(val)


#print(out)

####without using lrn function
def sortlsl():
    datacpy=listdata[:]
    out=[]
    while datacpy:
        val=datacpy[0]
        for d in datacpy:
            if d>val:
                val=d
        if val not in out:
            out.append(val)
        datacpy.remove(val)


    print(out)

    print("largest",out[0])

    print("secontlargest",out[1])
    
#sortlsl()
def checkl2l():
    datacpy2=listdata[:]
    largest=None
    secmall=None
    for d in datacpy2:
        if largest is None or d>largest:
            secmall=largest
            largest=d
        elif secmall is None or (d>secmall and d<largest):
            secmall=d
    print(largest)
    print(secmall)
    
checkl2l()
                

