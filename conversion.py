from datas import listdata

n=len(listdata)
listdatacpy=listdata
out=[]
for x in range(n):
    for y in range(n-1):
        if listdata[y]>listdata[y+1]:
            listdata[y],listdata[y+1]=listdata[y+1],listdata[y]


for val in listdata:
    if val not in out:
        out.append(val)


print(out)