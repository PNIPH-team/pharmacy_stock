# Code Main Function File
# Import Library and functions
from functions.connect_database import connect_database
from functions.category_options import category_options, listOfOptionsErrors
from functions.module.get_org_data import get_org_data
from functions.module.store_data import store_data
from functions.module.update import updateData
from functions.api import get_all_time_entries, store_logs, new_tei_values, post_analytic
from datetime import datetime
import time
from functions.files import return_path, create_file, write_file
import json
from config import today_date


def main(max_Number_Of_Loop):
    """
    Entry point of the program. Executes the main workflow.

    Args:
        max_Number_Of_Loop (int): Maximum number of loops.

    Returns:
        None
    """
    print(today_date)
    start_time = time.time()
    current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    print("Start Time:", current_time)
    # connect with local database Mysql with credentials
    connection, cursor = connect_database()
    # check if category options updated or not
    category_options()
    # for loop for all org and get list of updated event by date (today date)
    event_data = get_org_data(max_Number_Of_Loop)
    write_file(return_path()+'/data/tei_data_all.json', event_data)
    # Write the merged data back to the JSON file
    if len(new_tei_values) > 0:
        with open(return_path()+'/data/tei_data.json', 'r') as file:
            existing_data = json.load(file)

        data = [{
            "lastUpdated": last_updated,
            "orgUnit": org_unit,
            "trackedEntityInstance": tracked_entity
        } for last_updated, org_unit, tracked_entity in new_tei_values]
        existing_data = existing_data[0]['tei']
        existing_data += data
        tei_store_data = json.dumps(
            [{"tei": existing_data}], sort_keys=True, indent=4)
        write_file(return_path()+'/data/tei_data.json',
                  json.loads(tei_store_data))

    # with open(return_path()+'/data/tei_data_all.json', 'r') as file_tei:
    #     event_data = json.load(file_tei)
    # check event list if empty or not
    if not len(event_data) == 0:
        # get all event as list from all dhis2 organizations
        store_array = store_data(event_data, connection, cursor)
        # update event file
        get_all_time_entries()
        # update event data
        updateData(store_array)
    else:
        pass

    store_logs(current_time, event_data)
    print("An exception occurred", json.dumps(listOfOptionsErrors))

    # Write the merged data back to the JSON file
    if len(new_tei_values) > 0:
        with open(return_path()+'/data/tei_data.json', 'r') as file:
            existing_data = json.load(file)

        data = [{
            "lastUpdated": last_updated,
            "orgUnit": org_unit,
            "trackedEntityInstance": tracked_entity
        } for last_updated, org_unit, tracked_entity in new_tei_values]
        existing_data = existing_data[0]['tei']
        existing_data += data
        tei_store_data = json.dumps(
            [{"tei": existing_data}], sort_keys=True, indent=4)
        write_file(return_path()+'/data/tei_data.json',
                  json.loads(tei_store_data))
    print("End Time:", time.time())
    print("--- %s Minutes ---" % (time.time() - start_time))
    print(post_analytic())


# run main function
if __name__ == "__main__":
    max_Number_Of_Loop = 0
    while(max_Number_Of_Loop<1000):
        max_Number_Of_Loop+=100
        print(max_Number_Of_Loop)
        main(max_Number_Of_Loop)