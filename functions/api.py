# Define all API request to connect dhis2 with python for create, update and get data
import requests
from requests.auth import HTTPBasicAuth
import json
from config import dhis_password, dhis_url, dhis_user, today_date
from .files import writefile

# Create event on dhis2


def create_event(org_unit_id, quantity_before_exchange, medicine_id):
    data = {
        "status": "ACTIVE",
        "program": "fnIEoaflGxX",
        "enrollment": "lzL2rq6vcqw",
        "enrollmentStatus": "ACTIVE",
        "orgUnit": org_unit_id,
        "eventDate": today_date,
        "dataValues": [
            {
                "value": quantity_before_exchange,
                "dataElement": "LijzB622Z22"
            },
            {
                "dataElement": "bry41dJZ99x",
                "value": -quantity_before_exchange,
            },
        ],
        "attributeCategoryOptions": medicine_id
    }
    headers = {'Content-Type': 'application/json'}

    create_event = requests.post(dhis_url+"/api/events",
                                 data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(dhis_user, dhis_password))
    # print(create_event.request.body)
    att_req_data = json.loads(create_event.text)
    return att_req_data

def new_update_event(medication_id,total_quantity,quantity_stock,stock_quantity_dispensed,event_id,organisation_id,program_id,status):
    headers = {'Content-Type': 'application/json'}
    event_data = {
        "attributeCategoryOptions": medication_id,
        "status": status,
        "dataValues": [
            {
                "dataElement": "bry41dJZ99x",
                "value": int(total_quantity)
            },
                        {
                "dataElement": "eskqGfai0gc",
                "value": int(quantity_stock)
            },
            {
                "dataElement": "LijzB622Z22",
                "value": int(stock_quantity_dispensed)
            }
        ],
        "event": event_id,
        "orgUnit": organisation_id,
        "program": program_id
    }
    # print(json.dumps(event_data))
    try:
        update_event = requests.put(dhis_url+"/api/events/"+event_id, data=json.dumps(event_data),
                                    headers=headers, auth=HTTPBasicAuth(dhis_user, dhis_password))
        update_request_response = json.loads(update_event.text)
        # print(json.dumps(update_request_response))
        # print("Update Event Stock Successfully")
        return True
    except:
        # print("An exception occurred")
        return False

# Get all dhis2 event & store it on json


def get_all_time_entries():
    # TODO:: last check
    url_address = dhis_url+"/api/events?pageSize=10000&program=fnIEoaflGxX&order=eventDate:desc"
    headers = {'Content-Type': 'application/json'}

    # find out total number of pages
    r = requests.get(url=url_address, headers=headers,
                     auth=HTTPBasicAuth(dhis_user, dhis_password)).json()
    total_pages = int(r['pager']['pageCount'])

    # results will be appended to this list
    all_time_entries = []

    # loop through all pages and return JSON object
    for page in range(0, total_pages):

        url = dhis_url+"/api/events?page=" + \
            str(page)+"&pageSize=10000&program=fnIEoaflGxX&order=eventDate:desc"
        response = requests.get(url=url, headers=headers, auth=HTTPBasicAuth(
            dhis_user, dhis_password)).json()
        all_time_entries.append(response)
        page += 1

    # prettify JSON
    data = json.dumps(all_time_entries, sort_keys=True, indent=4)
    writefile('data/events.json', json.loads(data))

# Get all org


def get_org_req():
    get_org_unit_req = requests.get(
        dhis_url+"/api/programs/vj5cpA2OOfZ?fields=organisationUnits",
        auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_org_unit_req.text

# Get all tei for all org


def get_tei_org(org_unit_id):
    get_tei = requests.get(
        dhis_url+"/api/trackedEntityInstances?ou=" +
        org_unit_id+"&fields=trackedEntityInstance&lastUpdatedEndDate="
        + today_date + "&lastUpdatedStartDate=" + today_date,
        auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_tei.text

# Get all event for every tei


def get_event(tei_id):
    get_event = requests.get(
        dhis_url+"/api/events?trackedEntityInstance=" + tei_id + "&fields=event,orgUnit,program",
        auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_event.text

# Get all data for every event


def get_event_data(event_id):
    get_event_id = requests.get(
        dhis_url+"/api/events/" + event_id, auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_event_id.text
