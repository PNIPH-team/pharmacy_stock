import os
import json

def createFiles(path):
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)

def writefile(FileName, Data):
    json_data = json.dumps(Data, ensure_ascii=False)
    file = open(FileName, "w")
    with open(file.name, "w") as files:
        files.write(json_data)
    file.close()