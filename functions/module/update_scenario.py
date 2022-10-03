from ..api import create_event, new_update_event

def update_scenario(quantity_before_exchange,array_for_active_events,array_for_negative_values,org_unit_id,medicine_id):
    sorted_date_array = sorted(array_for_active_events, key=lambda x: x['date'])
    sorted_date_array_negative = sorted(array_for_negative_values, key=lambda x: x['date'],reverse=True)
    while quantity_before_exchange!=0:
        # print("val"+ str(quantity_before_exchange))
        
    # No Edit Scenario
        if(quantity_before_exchange==0):
            # print(quantity_before_exchange)
            pass

    # Positive Scenario
        elif(quantity_before_exchange>0):
            #* print("Edit Positive")
            #? Create New Event
            if(len(sorted_date_array)==0 and quantity_before_exchange !=0 ):
                # print('Number of active event is zero')
                create_event(org_unit_id,quantity_before_exchange,medicine_id)
                quantity_before_exchange=0
                continue

            #? Update Existed Event
            elif(len(sorted_date_array)>0):
                # print('>')
                #sort array by date from old to new
                for sorted_event_number in range(len(sorted_date_array)):
                    # set variables
                    event_id=sorted_date_array[0]['event']
                    organisation_id=sorted_date_array[0]['query']['orgUnit']
                    program_id=sorted_date_array[0]['query']['program']
                    quantity_stock=sorted_date_array[0]['quantity_stock']
                    stock_quantity_dispensed=sorted_date_array[0]['stock_quantity_dispensed']
                    medication_id=sorted_date_array[0]['query']['attributeCategoryOptions']
                    stock_total=sorted_date_array[0]['stock_total']
                    # calculate quantity 
                    calculation_value=quantity_before_exchange-stock_total # 108 - 80 = 28 # 280 - -250
                    if stock_quantity_dispensed is None:
                        stock_quantity_dispensed=0
                    if stock_total is None:
                        stock_total=0
                    if quantity_stock is None:
                        quantity_stock=0
                    # when event not enough
                    if(calculation_value>0):
                        # its just means this event not en.  
                        # set new stock dispensed value equal old dispensed plus total of stock
                        new_stock_quantity_dispensed=(stock_quantity_dispensed+stock_total) # 20+80
                        # set new total of quentity equal old quantity minus new stock dispensed
                        total_quantity=quantity_stock-new_stock_quantity_dispensed
                        new_update_event(medication_id,total_quantity,quantity_stock,new_stock_quantity_dispensed,event_id,organisation_id,program_id,"COMPLETED")
                        quantity_before_exchange=calculation_value #28
                        sorted_date_array.pop(0)
                        if(len(sorted_date_array)==0):
                            break
                        else:
                            continue
                    else:
                    # when event total is enough or minus
                        new_stock_quantity_dispensed=(stock_quantity_dispensed+quantity_before_exchange) # 72+28=100
                        total_quantity=quantity_stock-new_stock_quantity_dispensed
                        new_update_event(medication_id,total_quantity,quantity_stock,new_stock_quantity_dispensed,event_id,organisation_id,program_id,"ACTIVE")
                        quantity_before_exchange=0
                        break
                        
    # Negative Scenario
        elif(quantity_before_exchange<0):
            # print("Edit Negative")
            #? Create New Event
            if(len(sorted_date_array_negative)==0 and quantity_before_exchange !=0 ):
                # print('Number of negative event is zero')
                create_event(org_unit_id,quantity_before_exchange,medicine_id)
                quantity_before_exchange=0
                continue
            
            # Update Exist Event
            elif(len(sorted_date_array_negative)>0):
                # print('<')
              
                #sort array by date from old to new
                for negative_sorted_event_number in range(len(sorted_date_array_negative)):
                    # set variables
                    event_id=sorted_date_array_negative[0]['event']
                    organisation_id=sorted_date_array_negative[0]['query']['orgUnit']
                    program_id=sorted_date_array_negative[0]['query']['program']
                    quantity_stock=sorted_date_array_negative[0]['quantity_stock']
                    stock_quantity_dispensed=sorted_date_array_negative[0]['stock_quantity_dispensed']
                    if(stock_quantity_dispensed is None):
                        stock_quantity_dispensed=0
                    medication_id=sorted_date_array_negative[0]['query']['attributeCategoryOptions']
                    stock_total=sorted_date_array_negative[0]['stock_total']
                    # calculate quantity 
                    print("quantity_before_exchange")
                    print(quantity_before_exchange)
                    print("stock_quantity_dispensed")
                    print(stock_quantity_dispensed)
                    calculation_value=quantity_before_exchange+stock_quantity_dispensed # -250+50 =-200 + 200 // -180 + 200= 20
                    if stock_quantity_dispensed is None:
                        stock_quantity_dispensed=0
                    if stock_total is None:
                        stock_total=0
                    if quantity_stock is None:
                        quantity_stock=0

                    # when event not enough
                    if(calculation_value<0):
                        # its just means this event not en.  
                        # set new stock dispensed value equal old dispensed plus total of stock
                        new_stock_quantity_dispensed=0 # 60-40 # 60
                        # set new total of quentity equal old quantity minus new stock dispensed
                        total_quantity=quantity_stock # 100-100
                        new_update_event(medication_id,total_quantity,quantity_stock,new_stock_quantity_dispensed,event_id,organisation_id,program_id,"ACTIVE")
                        quantity_before_exchange=calculation_value #28
                        sorted_date_array_negative.pop(0)
                        if(len(sorted_date_array_negative)==0):
                            break
                        else:
                            continue
                    else:
                    # when event total is enough or minus
                        new_stock_quantity_dispensed=(stock_quantity_dispensed+quantity_before_exchange) # 80 +-80 = 0
                        total_quantity=quantity_stock-new_stock_quantity_dispensed # 0-80=-80
                        new_update_event(medication_id,total_quantity,quantity_stock,new_stock_quantity_dispensed,event_id,organisation_id,program_id,"ACTIVE")
                        quantity_before_exchange=0
                        break


