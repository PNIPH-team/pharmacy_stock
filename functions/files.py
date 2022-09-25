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
    file = open(file_name, "w")
    with open(file.name, "w") as files:
        files.write(json_data)
    file.close()