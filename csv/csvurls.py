import csv
import sys
import os


def main():
    list= os.listdir()                          #files in same dir
    data=""                                     #save read data from csv
    target=""                                   #target csv file
    col= "identifier"                           #column to extract data from
    output= "urls.txt"                          #output file name
    if(len(sys.argv())==4):
        target=sys.argv[1]
        col= sys.argv[2]
        output=sys.argv[3]
    
    for file in list:
        if(file.find('.csv')!=-1):              #get first csv file
            target=file
            break
    with open(target, newline='\n') as csvfile: #open csv
        reader = csv.DictReader(csvfile)
        for row in reader:
            data+=row[col].strip()+'\n'
    f = open("scopeurls.txt","a")
    for i in data:
        f.write(i)
    

if __name__ == "__main__":
    main()