# Define all API request to connect dhis2 with python for create, update and get data
import requests
from requests.auth import HTTPBasicAuth
import json
from config import dhis_password, dhis_url, dhis_user, today_date, programId, programIdStock, dataElementForQuantity, dataElementForTotalQuantity, dataElementForQuantityStock
from .files import write_file, return_path, create_file

# Create event on dhis2
post_log = []
put_log = []
new_tei_values = []


def store_logs(date, array):
    """
    Stores logs in files for a specific date.

    Parameters:
    - date (str): The date for which the logs are being stored.
    - array (list): The log data to be stored.

    Returns:
    None
    """
    create_file(return_path()+'/data/'+date)
    write_file(return_path()+'/data/'+date+'/post_log.json', post_log)
    write_file(return_path()+'/data/'+date+'/put_log.json', put_log)
    write_file(return_path()+'/data/'+date+'/data_log.json', array)
    post_log.clear()
    put_log.clear()


def create_event(org_unit_id, quantity_before_exchange, medicine_id):
    """
    Creates an event in DHIS2 for a given organization unit, quantity, and medicine ID.

    Parameters:
    - org_unit_id (str): The ID of the organization unit.
    - quantity_before_exchange (int): The quantity before exchange.
    - medicine_id (str): The ID of the medicine.

    Returns:
    dict: The response data from the DHIS2 API for the created event.
    """
    data = {
        "status": "ACTIVE",
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
    """
    Updates an existing event in DHIS2 with new data.

    Parameters:
    - medication_id (str): The ID of the medication.
    - total_quantity (int): The total quantity of the medication.
    - quantity_stock (int): The quantity in stock.
    - stock_quantity_dispensed (int): The quantity of stock dispensed.
    - event_id (str): The ID of the event to be updated.
    - organisation_id (str): The ID of the organization unit.
    - program_id (str): The ID of the program.
    - status (str): The status of the event.
    - expire_date (datetime): The expiration date of the medication (optional).

    Returns:
    - bool: True if the event update was successful, False otherwise.
    """

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


def get_all_time_entries():
    """
    Retrieves all events from DHIS2 and stores them in a JSON file.

    Returns:
    - None
    """
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
    write_file(return_path()+'/data/events.json', json.loads(data))


def get_org_req():
    """
    Retrieves the organization units associated with a specific program from DHIS2.

    Returns:
    - The response text of the HTTP request.
    """
    get_org_unit_req = requests.get(
        dhis_url+"/api/programs/"+programId+"?fields=organisationUnits",
        auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_org_unit_req.text


def get_tei_org(org_unit_id, startUpdateDate, endUpdateDate):
    """
    Retrieves tracked entity instances (TEIs) from DHIS2 based on the specified organization unit,
    start update date, and end update date. Compares the retrieved TEIs with the stored TEI data
    to identify any missing values. Returns the list of missing TEIs.

    Parameters:
    - org_unit_id: The ID of the organization unit to retrieve TEIs for.
    - startUpdateDate: The start date for filtering TEIs based on their last updated date.
    - endUpdateDate: The end date for filtering TEIs based on their last updated date.

    Returns:
    - A JSON string containing the list of missing TEIs.
    """
    all_tei = []
    page = 1
    while True:
        # Make API call
        get_tei = requests.get(
            dhis_url+"/api/trackedEntityInstances?ou=" +
            org_unit_id+"&program="+programId+"&fields=trackedEntityInstance,lastUpdated,orgUnit&lastUpdatedStartDate=" +
            startUpdateDate+"&lastUpdatedEndDate=" +
            endUpdateDate+"&page=" + str(page),
            auth=HTTPBasicAuth(dhis_user, dhis_password))
        # Check if response is empty
        if not get_tei.json()['trackedEntityInstances']:
            break

        # Append results to all_tei list
        all_tei += get_tei.json()['trackedEntityInstances']

        # Increment page number
        page += 1

    # loop on list tei_list with Monthly Array
    with open(return_path()+'/data/tei_data.json', 'r') as tei_file:
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


def get_event(tei_id):
    """
    Retrieves events associated with a specific tracked entity instance (TEI) from DHIS2.

    Parameters:
    - tei_id: The ID of the tracked entity instance to retrieve events for.

    Returns:
    - The response text containing the retrieved events.
    """
    get_event = requests.get(
        dhis_url+"/api/events?trackedEntityInstance=" +
        tei_id + "&fields=event,orgUnit,program&pageSize=10000",
        auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_event.text


def get_event_data(event_id):
    """
    Retrieves the data of a specific event from DHIS2 based on the event ID.

    Parameters:
    - event_id: The ID of the event to retrieve the data for.

    Returns:
    - The response text containing the event data.
    """
    get_event_id = requests.get(
        dhis_url+"/api/events/" + event_id, auth=HTTPBasicAuth(dhis_user, dhis_password))
    return get_event_id.text


def post_analytic():
    """
    Runs analytics on DHIS2 to generate resource tables for all data.

    Returns:
    - A success message if the analytics request was successful.
    - A tuple containing an error message and the status code if the request failed.
    """
    post_analytic_request = requests.post(
        dhis_url+"/api/39/resourceTables/analytics", auth=HTTPBasicAuth(dhis_user, dhis_password))
    # Check the response status code
    if post_analytic_request.status_code == 200:
        return "Run Analytics successful!"
    else:
        return ("Request failed with status code:", post_analytic_request.status_code)
