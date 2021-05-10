var={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
a=[]
b=[]
for key in var:
    a.append(key)
    b.append(var[key])
    # print(a)
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
        if b[i]<b[j]:
            b[i],b[j]=b[j],b[i]
var1={}
for k in range(0,len(a)):
    var1[a[k]]=b[k]
import json
with open("que4.json","w") as jsonfile:
    json.dump(var1,jsonfile,indent=4)














