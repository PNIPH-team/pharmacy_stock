from datetime import datetime
from config import today,dataElementForQuantity,dataElementForTotalQuantity,dataElementForQuantityStock

def split_events(quantity_before_exchange,filter_events_by_medication_organization):
    #define Arrays
    array_for_active_events=[]
    array_for_not_active_events=[]
    array_for_negative_values=[]
    # Check exchange value if not zero else print zero
    if(quantity_before_exchange>0 or quantity_before_exchange<0):
        # loop on all met the conditions events
        for dic in filter_events_by_medication_organization:
            # Set variables with default values
            event_status_active=False
            not_expired=True
            event_stock_quantity_dispensed=None
            event_stock_total=None
            event_quantity_stock=None
            event_expire_date_value=None
            # Check event status
            if(dic['status']=='ACTIVE'):
                event_status_active=True
            
            # Loop on all data values
            for data_value_loop_three_number in range(len(dic['dataValues'])):
                # Check if event expired or not else not expired
                if(dic['dataValues'][data_value_loop_three_number]['dataElement']=='xW95VLnIqyP'):
                    event_expire_date_value = datetime.strptime(dic['dataValues'][data_value_loop_three_number]['value'], '%Y-%m-%d').date()
                    event_today_date_value =  datetime.strptime(today.strftime( '%Y-%m-%d'), '%Y-%m-%d').date()
                    if(event_today_date_value<=event_expire_date_value):
                        not_expired=True
                    else:
                        not_expired=False
                
                # Store event dispensed stock quantity value
                if(dic['dataValues'][data_value_loop_three_number]['dataElement']==dataElementForQuantity):
                    event_stock_quantity_dispensed=int(dic['dataValues'][data_value_loop_three_number]['value'])
                
                # Store event total stock value
                if(dic['dataValues'][data_value_loop_three_number]['dataElement']==dataElementForTotalQuantity):
                    event_stock_total=int(dic['dataValues'][data_value_loop_three_number]['value'])
                
                # Store event stock quantity value
                if(dic['dataValues'][data_value_loop_three_number]['dataElement']==dataElementForQuantityStock):
                    event_quantity_stock=int(dic['dataValues'][data_value_loop_three_number]['value'])

            # Check and add to lists        
            if(event_status_active and  not_expired):
                array_for_active_events.append({"event":dic['event'],"date":datetime.strptime(dic['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"expire":event_expire_date_value,"stock_quantity_dispensed":event_stock_quantity_dispensed,"stock_total":event_stock_total,"quantity_stock":event_quantity_stock,"query":dic})
                array_for_negative_values.append({"event":dic['event'],"date":datetime.strptime(dic['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"expire":event_expire_date_value,"stock_quantity_dispensed":event_stock_quantity_dispensed,"stock_total":event_stock_total,"quantity_stock":event_quantity_stock,"query":dic})
            else:
                # check data of stock inventory
                array_for_not_active_events.append({"event": dic['event'] ,"date":datetime.strptime(dic['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"expire":event_expire_date_value,"stock_quantity_dispensed":event_stock_quantity_dispensed,"stock_total":event_stock_total,"quantity_stock":event_quantity_stock,"query":dic})
                array_for_negative_values.append({"event":dic['event'],"date":datetime.strptime(dic['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"expire":event_expire_date_value,"stock_quantity_dispensed":event_stock_quantity_dispensed,"stock_total":event_stock_total,"quantity_stock":event_quantity_stock,"query":dic})

    return array_for_active_events,array_for_not_active_events,array_for_negative_values