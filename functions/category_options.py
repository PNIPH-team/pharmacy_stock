# Define all function related with category options
import requests
from requests.auth import HTTPBasicAuth
import json
from .files import writefile,pathReturn,readfile
from config import dhis_url,dhis_user,dhis_password
import os

categoryOptionsList = []
listOfOptionsErrors = []

# this function to loop on all args & store data to list
def store_category(args):
    for category_data in args:
        categoryOptionsList.append(category_data)

# this fucntion to get all gategory options from dhis2 and store it on category file to use it later
def category_options():
    # load existing category options from JSON file
    existing_data = readfile(pathReturn()+'/data/categoryOptions.json')

    # request to get first page of category options data
    category_options_req = requests.get(
        dhis_url+"/api/categoryOptions?fields=id,code&pageSize=50",
        auth=HTTPBasicAuth(dhis_user, dhis_password)).json()

    # merge new data with existing data
    all_data = []
    while True:
        for category in category_options_req["categoryOptions"]:
            # check if category option already exists in existing data
            existing_category = next((c for c in existing_data if c["code"] == category["code"]), None)

            if existing_category is None:
                # add new category option data to existing data
                all_data.append(category)
            else:
                # update existing category option data
                existing_category.update(category)
                all_data.append(existing_category)

        # write data to JSON file
        writefile(pathReturn()+'/data/categoryOptions.json', all_data)

        # check if there are more pages of data
        if category_options_req["pager"]["page"] == category_options_req["pager"]["pageCount"]:
            break

        # make request for next page of data
        next_page_url = category_options_req["pager"]["nextPage"]
        category_options_req = requests.get(next_page_url, auth=HTTPBasicAuth(dhis_user, dhis_password)).json()

    return all_data


def get_code_data(medicine_name):
    try:
        with open(pathReturn()+'/data/categoryOptions.json') as categoryOptionsFile:
         catFile = json.load(categoryOptionsFile)
         MappingList=list(filter(lambda x:x["code"]==medicine_name,catFile))
         return MappingList[0]['id']
    except:
        listOfOptionsErrors.append(medicine_name)



