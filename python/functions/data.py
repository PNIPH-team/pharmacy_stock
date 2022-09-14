


# check if args is not null
def check(args):
    if(args=='' or args==None):
        return None
    else:
        return args

        

def insert_new(medicine_value, quantity_value,data_element,newest_data,numberOfNewData):
    the_big_data_array = {"tei": newest_data[numberOfNewData]['tei'], "program": newest_data[numberOfNewData]['program'],
                            "orgunit": newest_data[numberOfNewData]['orgunit'], "date": newest_data[numberOfNewData]['date'],"dataElement":data_element, "m": medicine_value,
                            "q": quantity_value,"edit_date": newest_data[numberOfNewData]['last_update']}
    return the_big_data_array
    # the_big_data_newest_list.append(the_big_data_array)
