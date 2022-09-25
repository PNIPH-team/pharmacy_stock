import requests
from requests.auth import HTTPBasicAuth
import json

categoryOptionsList = []
# this function to loop on all args & store data to list
def store_category(args):
    for category_data in args:
        categoryOptionsList.append(category_data)

def category_options(dhis_url,dhis_user,dhis_password):
    # request to get category options data
    category_options_req = requests.get(
        dhis_url+"/api/categoryOptions?fields=id,code",
        auth=HTTPBasicAuth(dhis_user, dhis_password)).json()
    # add data to list
    store_category(category_options_req["categoryOptions"])
    # loop to get all pages from api
    while category_options_req["pager"]['pageCount'] != category_options_req["pager"]['page']:
        category_options_req = requests.get(
            category_options_req["pager"]['nextPage'], auth=HTTPBasicAuth(dhis_user, dhis_password)).json()
        store_category(category_options_req["categoryOptions"])
    return categoryOptionsList
    # writefile("categoryOptions.json", categoryOptionsList)



def get_code_data(medicine_name):
    with open('categoryOptions.json') as categoryOptionsFile:
         catFile = json.load(categoryOptionsFile)
         MappingList=list(filter(lambda x:x["code"]==medicine_name,catFile))
         return MappingList[0]['id']



