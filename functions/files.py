# Define all create and write files functions
import os
import json

# create files with path parameters
def createFiles(path):
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)

# write data on file with file path and data parameters
def writefile(file_name, data):
    json_data = json.dumps(data, ensure_ascii=False)
    if (os.path.exists(file_name)):
        os.remove(file_name)
    file = open(file_name, "w")
    with open(file.name, "w") as files:
        files.write(json_data)
    file.close()

def pathReturn():
    return "/home/script/pharmacy_stock"

def readfile(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
        return data
    else:
        return []