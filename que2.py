import json


name={
   'Name': 'Ram',
   'Class': 'IV',
   'Age': 9
}

out_file=open("que2.json","w")
json.dump(name,out_file,indent=4)
out_file.close()

