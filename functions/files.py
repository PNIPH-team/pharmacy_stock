# Define all create and write files functions
import os
import json

def create_file(path):
    """
    Creates a file at the specified path.

    Args:
    - path: The path where the file will be created.
    """
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)

def write_file(file_name, data):
    """
    Writes data to a file.

    Args:
    - file_name: The name of the file.
    - data: The data to be written to the file.
    """
    json_data = json.dumps(data, ensure_ascii=False)
    if (os.path.exists(file_name)):
        os.remove(file_name)
    file = open(file_name, "w")
    with open(file.name, "w") as files:
        files.write(json_data)
    file.close()

def return_path():
    """
    Returns the path where files are stored.
    """
    return "/Users/salehabbas/Documents/GitHub/pharmacy_stock"

def read_file(file_name):
    """
    Reads data from a file.

    Args:
    - file_name: The name of the file to read.

    Returns:
    - The data read from the file.
    - An empty list if the file does not exist.
    """
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
        return data
    else:
        return []