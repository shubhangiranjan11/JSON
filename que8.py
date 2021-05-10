import json
a=["neelam","programmer","24","24000"]
b=["komal","trainer","24","20000"]
c=["anuradha","hr","24","40000"]
d=["abhishek","manager","29","630000"]
e=["name","designation","age","salary"]
i=0
dict1={}
dict2={}
dict3={}
dict4={}
p={}
while i<len(a):
    j=0
    while j<len(a):
        dict1[e[i]]=a[j]
        dict2[e[i]]=b[j]
        dict3[e[i]]=c[j]
        dict4[e[i]]=d[j]
        j=j+1
    p["emp1"]=dict1
    p["emp2"]=dict2
    p["emp3"]=dict3
    p["emp3"]=dict4
    i=i+1
data=json.dumps(p,indent=4)
print(data)


