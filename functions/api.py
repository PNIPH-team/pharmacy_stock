# Define all API request to connect dhis2 with python for create, update and get data
import requests
from requests.auth import HTTPBasicAuth
import json
from config import dhis_password, dhis_url, dhis_user, today_date, programId, programIdStock, dataElementForQuantity, dataElementForTotalQuantity, dataElementForQuantityStock
from .files import writefile, pathReturn, createFiles, readfile
import os

# Create event on dhis2
post_log = []
put_log = []
new_tei_values = []


def store_logs(date, array):
    createFiles(pathReturn()+'/data/'+date)
    writefile(pathReturn()+'/data/'+date+'/post_log.json', post_log)
    writefile(pathReturn()+'/data/'+date+'/put_log.json', put_log)
    writefile(pathReturn()+'/data/'+date+'/data_log.json', array)
    post_log.clear()
    put_log.clear()


def create_event(org_unit_id, quantity_before_exchange, medicine_id):
    data = {
        "status": "COMPLETED",
        "program": programIdStock,
        "enrollment": "lzL2rq6vcqw",
        "enrollmentStatus": "ACTIVE",
        "orgUnit": org_unit_id,
        "eventDate": today_date,
        "dataValues": [
            {
                "value": quantity_before_exchange,
                "dataElement": dataElementForQuantity
            },
            {
                "dataElement": dataElementForTotalQuantity,
                "value": -quantity_before_exchange,
            },
        ],
        "attributeCategoryOptions": medicine_id
    }
    headers = {'Content-Type': 'application/json'}
    if(quantity_before_exchange != 0):
        create_event = requests.post(dhis_url+"/api/events",
                                     data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(dhis_user, dhis_password))
        att_req_data = json.loads(create_event.text)
        post_log.append({"data": att_req_data})
    return att_req_data


def new_update_event(medication_id, total_quantity, quantity_stock, stock_quantity_dispensed, event_id, organisation_id, program_id, status, expire_date):
    headers = {'Content-Type': 'application/json'}
    add_date = None
    if(expire_date != None):
        add_date = {
            "dataElement": "xW95VLnIqyP",
            "value": expire_date.strftime("%Y-%m-%d")
        }
    array_values = [
        {
            "dataElement": dataElementForTotalQuantity,
            "value": int(total_quantity)
        },
        {
            "dataElement": dataElementForQuantityStock,
            "value": int(quantity_stock)
        },
        {
            "dataElement": dataElementForQuantity,
            "value": int(stock_quantity_dispensed)
        }
    ]
    if(add_date != None):
        array_values.append(add_date)
    event_data = {
        "attributeCategoryOptions": medication_id,
        "status": status,
        "dataValues": array_values,
        "event": event_id,
        "orgUnit": organisation_id,
        "program": program_id
    }
    try:
        if(stock_quantity_dispensed != 0):
            update_event = requests.put(dhis_url+"/api/events/"+event_id, data=json.dumps(event_data),
                                        headers=headers, auth=HTTPBasicAuth(dhis_user, dhis_password))
            update_request_response = json.loads(update_event.text)
            put_log.append({"data": update_request_response})
        return True
    except:
        return False

# Get all dhis2 event & store it on json
def get_all_time_entries():
    url_address = f"{dhis_url}/api/events"
    headers = {'Content-Type': 'application/json'}

    # set page to 1 since there's no existing data
    page = 1
    # set all_time_entries to an empty list
    all_time_entries = []

    is_last_page = True

    while is_last_page:
        # set up query parameters for current page
        query_params = {
            "program": programIdStock,
            "fields": "event,attributeCategoryOptions,orgUnit,program,status,orgUnitName,eventDate,created,lastUpdated,dataValues",
            "pageSize": 10000,
            "page": page,
            "order": "eventDate:desc"
        }

        # make HTTP request
        response = requests.get(url=url_address, headers=headers, auth=HTTPBasicAuth(
            dhis_user, dhis_password), params=query_params).json()

        all_time_entries.extend(response['events'])
        # check if there are more pages§
        is_last_page = response["pager"]["isLastPage"]
        # increment page number for next iteration
        page += 1
    # write all data to JSON file
    data = json.dumps([{"events": all_time_entries}], sort_keys=True, indent=4)
    writefile(pathReturn()+'/data/events.json', json.loads(data))

#Get all org
def get_org_req():
    get_org_unit_req = requests.get(
        dhis_url+"/api/programs/"+programId+"?fields=organisationUnits",
        auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_org_unit_req.text

#Get all tei for all org
def get_tei_org(org_unit_id, startUpdateDate, endUpdateDate):
    all_tei = []
    page = 1
    while True:
        # Make API call
        get_tei = requests.get(
            dhis_url+"/api/trackedEntityInstances?ou=" +
            org_unit_id+"&program="+programId+"&fields=trackedEntityInstance,lastUpdated,orgUnit&page=" + str(page),
            auth=HTTPBasicAuth(dhis_user, dhis_password))
        # Check if response is empty
        if not get_tei.json()['trackedEntityInstances']:
            break

        # Append results to all_tei list
        all_tei += get_tei.json()['trackedEntityInstances']

        # Increment page number
        page += 1

    # loop on list tei_list with Monthly Array
    with open(pathReturn()+'/data/tei_data.json', 'r') as tei_file:
        tei_stored_data = json.load(tei_file)

    # Extract values to check
    json_values = [(item["lastUpdated"], item["orgUnit"], item["trackedEntityInstance"])
                   for item in tei_stored_data[0]['tei']]
    api_values = [(item["lastUpdated"], item["orgUnit"],
                   item["trackedEntityInstance"]) for item in all_tei]

    # Find missing values
    missing_values = [
        value for value in api_values if value not in json_values]
    if(len(missing_values) > 0):
        new_tei_values.extend(missing_values)
    # Extract list of TEI from all_tei
    tei_list = [tei[2] for tei in missing_values]

    # Return concatenated result
    print(json.dumps({"trackedEntityInstances": tei_list}))
    return json.dumps({"trackedEntityInstances": tei_list})

#Get all event for every tei
def get_event(tei_id):
    get_event = requests.get(
        dhis_url+"/api/events?trackedEntityInstance=" +
        tei_id + "&fields=event,orgUnit,program&pageSize=10000",
        auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_event.text

# Get all data for every event
def get_event_data(event_id):
    get_event_id = requests.get(
        dhis_url+"/api/events/" + event_id, auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_event_id.text
