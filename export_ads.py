import json
import sys

if len(sys.argv) != 3:
    print("Usage : export_ads.py [source file] [export file]")
    sys.exit()

file_path = sys.argv[1]
export = sys.argv[2]

jlist = []
ads = []
for line in open(file_path, 'r'):
    jlist.append(json.loads(line))

for i in range(len(jlist)):
    for j in range(len(jlist[i]["FilesLoaded"].split(','))):
        if(jlist[i]["FilesLoaded"].split(',')[j].find(':') != -1):
            ads.append({"ads": jlist[i]["FilesLoaded"].split(', ')[j]
            , "SourceFileName": jlist[i]["SourceFilename"]
            , "ExecutableName":jlist[i]["ExecutableName"]
            , "size": jlist[i]["Size"]
            , "count":jlist[i]["RunCount"]
            , "last run":jlist[i]["LastRun"]})

with open(export, 'w') as f:
    json.dump(ads, f, indent=2, ensure_ascii=False)