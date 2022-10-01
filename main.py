# Code Main Function File
# Import Library and functions
import os
from functions.connect_database import connect_database
from functions.category_options import category_options
from functions.module.get_org_data import get_org_data
from functions.module.store_data import store_data
from functions.module.update import updateData
from functions.api import get_all_time_entries
import json
# define main function
def main():
    #connect with local database Mysql with credentials 
    connection,cursor = connect_database()
    # check if category options updated or not
    # if not os.path.exists('data/categoryOptions.json'):
    #     category_options()
    # #for loop for all org and get list of updated event by date (today date)
    # event_data=get_org_data()

    # check event list if empty or not
    # if not len(event_data) == 0:
    #     # get all event as list from all dhis2 organizations
    #     store_array=store_data(event_data,connection,cursor)
    #     print(store_array)
    #     # store_array=[{"orgunit": "ORsMYiLzFC9", "m": "n34JlJWVzHx", "q": "20"}]
    #     # update event file
    #     get_all_time_entries()
    #     # update event data
    #     updateData(store_array)
    # else:
    #     # print empty if no new event found
    #     print("Empty Data *No New Data Found")
    get_all_time_entries()
    updateData(json.dumps([{"orgunit": "ORsMYiLzFC9", "m": "n34JlJWVzHx", "q": "550"},{"orgunit": "k3jhRofJS7G", "m": "n34JlJWVzHx", "q": "500"}]))


# run main function
if __name__ == "__main__":
    main()