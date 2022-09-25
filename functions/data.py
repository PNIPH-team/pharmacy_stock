# Define function to check and insert data

# check if args is not null
def check(args):
    if(args=='' or args==None):
        return None
    else:
        return args

# insert function have multi parameter and return object with event data
def insert_new(medicine_value, quantity_value,data_element,newest_data):
    the_big_data_array = {"event_id": newest_data['event_id'],"tei": newest_data['tei'], "program": newest_data['program'],"stage": newest_data['stage'],
                            "orgunit": newest_data['orgunit'], "date": newest_data['date'],"dataElement":data_element, "m": medicine_value,
                            "q": quantity_value,"edit_date": newest_data['last_update']}
    return the_big_data_array
