import sys
import os
#sort data alphabetically
f=open(sys.argv[1],"r")
data=f.readlines()
list(set(data))
data.sort()
for i in range(len(data)):
    if(data[i].isspace()):
        data.pop(i)
newdata= "".join(data)
f=open(sys.argv[1],"w")
f.write(newdata)