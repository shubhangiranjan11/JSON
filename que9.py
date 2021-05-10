import json
a={"shopping list":{"chaco":"20","biscuits":"50","diary_milk":"30","ice_cream":"20"}}
user1=int(input("enter your item quantity="))
item=input("enter any key=")
c=a["shopping list"][item]
b=int(c)-user1
a["shopping list"][item]=b
d=json.dumps(a)
print(d)

