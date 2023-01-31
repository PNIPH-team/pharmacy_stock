# Code Main Function File
# Import Library and functions
import os
from functions.connect_database import connect_database
from functions.category_options import category_options
from functions.module.get_org_data import get_org_data
from functions.module.store_data import store_data
from functions.module.update import updateData
from functions.api import get_all_time_entries,store_logs
import schedule
import time
from functions.files import pathReturn,createFiles
from config import current_time

# define main function
def main():
    start_time = time.time()
    print("Start Time:",current_time)
    #connect with local database Mysql with credentials 
    connection,cursor = connect_database()
    # check if category options updated or not
    if not os.path.exists(pathReturn()+'/data/categoryOptions.json'):
        category_options()
    # #for loop for all org and get list of updated event by date (today date)
    event_data=get_org_data()
    # check event list if empty or not
    if not len(event_data) == 0:
        # get all event as list from all dhis2 organizations
        print("event_data",event_data)
        store_array=store_data(event_data,connection,cursor)
        print("store_array",store_array)
        # update event file
        print("GetData")
        get_all_time_entries()
        # update event data
        updateData(store_array)
    else:
        pass
    store_logs(current_time)
    print("End Time:",time.time())
    print("--- %s seconds ---" % (time.time() - start_time))

# run main function
if __name__ == "__main__":
    main()