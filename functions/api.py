# Define all API request to connect dhis2 with python for create, update and get data
import requests
from requests.auth import HTTPBasicAuth
import json
from config import dhis_password,dhis_url,dhis_user,today_date
from .files import writefile
create_response_array=[]

# Create event on dhis2
def create_event(org_unit_id,previouse_exchange_value,medicine_id):
        data = {
                        "status": "ACTIVE",
                        "program": "fnIEoaflGxX",
                        "enrollment": "lzL2rq6vcqw",
                        "enrollmentStatus": "ACTIVE",
                        "orgUnit": org_unit_id,
                        "eventDate": today_date,
                        "dataValues": [
                            {
                                "value": previouse_exchange_value,
                                "dataElement": "LijzB622Z22"
                            },
                             {
                                "dataElement": "bry41dJZ99x",
                                "value": -previouse_exchange_value,
                            },
                        ],
                        "attributeCategoryOptions": medicine_id
                    }
        headers = {'Content-Type': 'application/json'}

        create_event = requests.post(dhis_url+"/api/events",
                                        data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(dhis_user, dhis_password))
        print(create_event.request.body)
        att_req_data = json.loads(create_event.text)
        create_response_array.append(att_req_data)
        # print("Create Stock Successfully")
        # print(att_req_data)
        return att_req_data

# Update exist event on dhis2
def update_event(event_id,event_data):
    print(event_id)
    print(event_data)
    headers = {'Content-Type': 'application/json'}
    try:
        update_event = requests.put(dhis_url+"/api/events/"+event_id, data =event_data,headers=headers, auth=HTTPBasicAuth(dhis_user, dhis_password))
        update_request_response = json.loads(update_event.text)
        print(json.dumps(update_request_response))
        print("Update Event Stock Successfully")
    except:
        print("An exception occurred")

# Get all dhis2 event & store it on json
def get_all_time_entries():
    url_address = dhis_url+"/api/events?program=fnIEoaflGxX"  
    headers = {'Content-Type': 'application/json'}

    # find out total number of pages
    r = requests.get(url=url_address, headers=headers, auth=HTTPBasicAuth(dhis_user, dhis_password)).json()
    total_pages = int(r['pager']['pageCount'])

    # results will be appended to this list
    all_time_entries = []

    # loop through all pages and return JSON object
    for page in range(0, total_pages):

        url = dhis_url+"/api/events?page="+str(page)+"&program=fnIEoaflGxX"              
        response = requests.get(url=url, headers=headers, auth=HTTPBasicAuth(dhis_user, dhis_password)).json()        
        all_time_entries.append(response)       
        page += 1

    # prettify JSON
    data = json.dumps(all_time_entries, sort_keys=True, indent=4)
    writefile('data/events.json',json.loads(data))

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
                    dhis_url+"/api/events?trackedEntityInstance=" + tei_id + "&lastUpdatedEndDate=" +
                    today_date + "&lastUpdatedStartDate=" + today_date + "&fields=event,orgUnit,program",
                    auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_event.text

# Get all data for every event
def get_event_data(event_id):
    get_event_id = requests.get(
                        dhis_url+"/api/events/" + event_id, auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_event_id.text