import sys
import json
import os

def single(filename):       #gets urls with specific status
    f=open(filename,"r")
    data=f.readlines()
    res=""
    for i in data:
        if(i.startswith('{')):
            k=json.loads(i)
            stat=k["status"]
            print(stat)
            if(stat==200 or stat==302 or stat==401 or stat==403):
                res=res+i
    return res

def allfiles(directory):    #get filtered urls of all json in dir
    files=os.listdir(directory)
    combo=""
    for file in files:
        if(file.endswith('.json')):
            dat=single(f'{sys.argv[1]}/{file}')
            combo=combo+dat
    return combo

data=allfiles(sys.argv[1])

f=open("combined.txt","w")
f.write(data)
