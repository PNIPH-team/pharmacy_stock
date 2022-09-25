import os
from datetime import date
from datetime import datetime
import time

from functions.connect_database import connect_database
from functions.category_options import category_options
from functions.module.get_org_data import get_org_data
from functions.module.store_data import store_data
from functions.module.update import updateData
from functions.api import get_all_time_entries
def main():
    #connect with local database Mysql with credentials 
    connection,cursor = connect_database()
    # check if category options updated or not
    if not os.path.exists('categoryOptions.json'):
        category_options()
    #for loop for all org and get list of updated event by date (today date)
    event_data=get_org_data()
    # if array not empty
    if not len(event_data) == 0:
        store_array=store_data(event_data,connection,cursor)
        # update event file
        get_all_time_entries()
        # update event data
        print(updateData(store_array))
      #write array data to RowData File
        #   json.dumps(newest_data)
        # writefile(todayDateTime + "/RowData_" +
        #         today_date + ".json", json.loads(jsonStr))
    else:
        print("Empty Data *No New Data Found")
        # writefile(todayDateTime + "/JobSummary" +
        #         today_date + ".json", json.dumps([{"0": "EmptyData"}]))
if __name__ == "__main__":
    main()