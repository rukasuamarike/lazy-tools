import sys
import json
import os
#from json obj to url txt file
#geturl.py file.json
def single(filename):
    f=open(filename,"r")
    data=f.readlines()
    res=""
    for i in data:
        if(i.startswith('{')):
            k=json.loads(i)
            stat=k["output"]
            print(stat)
            res=res+stat+'\n'
    return res

data=single(sys.argv[1])

f=open("geturl.txt","w")
f.write(data)
