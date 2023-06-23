# Define function to check and insert data

# check if args is not null
def check(args):
    """
    Checks if the provided argument is empty or None.

    Args:
    - args: The argument to check.

    Returns:
    - None if the argument is empty or None.
    - The argument itself if it is not empty or None.
    """
    if(args=='' or args==None):
        return None
    else:
        return args

# insert function have multi parameter and return object with event data
def insert_new(medicine_value, quantity_value,data_element,newest_data):
    """
    Inserts new data into an event and returns an object with the event data.

    Args:
    - medicine_value: The value of the medicine.
    - quantity_value: The value of the quantity.
    - data_element: The data element to insert the values into.
    - newest_data: The newest data containing event information.

    Returns:
    - A dictionary containing the event data.
    """
    the_big_data_array = {"event_id": newest_data['event_id'],"tei": newest_data['tei'], "program": newest_data['program'],"stage": newest_data['stage'],
                            "orgunit": newest_data['orgunit'], "date": newest_data['date'],"dataElement":data_element, "m": medicine_value,
                            "q": quantity_value,"edit_date": newest_data['last_update']}
    return the_big_data_array
