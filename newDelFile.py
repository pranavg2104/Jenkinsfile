import os
import time
import json

def getLocationAndTime(location):
    store={}
    for root , directories , files in os.walk(location):
        for filename in files:
            filepath=os.path.join(root,filename)
            store[filepath]=os.stat(filepath).st_mtime
    return sorted(store.items(), key=lambda x:x[1])

def deleteFile(files,nFiles):
    keep=len(files)-nFiles
    for i in range(0,keep):
        os.remove(files[i][0])

with open('D:\Python Project\location.json') as l:
    loc=json.load(l)
    if os.path.exists(loc['build']['location']):
        files=getLocationAndTime(loc['build']['location'])
        deleteFile(files,loc['build']['numberOfFiles'])
    else:
        print("Enter a valid file location")
