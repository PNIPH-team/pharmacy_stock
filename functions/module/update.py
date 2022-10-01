# Define all type of action to reverse it to dhis2 system (capture)
import json
from datetime import datetime
from ..api import create_event, new_update_event,update_event
from config import today

# This function work to check every new event with existing event on capture program
def updateData(all_event_data_groupby_json):
    #Load last updated list from database
    group_by_database_array=json.loads(all_event_data_groupby_json)
    for group_by_database_list in range(len(group_by_database_array)):
        #define Arrays
        array_for_active_events=[]
        array_for_not_active_events=[]
        array_for_negative_values=[]

        #define variables from database data
        org_unit_id=group_by_database_array[group_by_database_list]['orgunit']
        medicine_id=group_by_database_array[group_by_database_list]['m']
        dispensed_quantity=group_by_database_array[group_by_database_list]['q']
        print("org_unit_id:",org_unit_id)
        print("medicine_id:",medicine_id)
        print("dispensed_quantity:",dispensed_quantity)
        complete_dispense_value=0
        active_dispense_value=0

        # read events data from json file
        with open('data/events.json') as event:
        # GET List of event for the same id
            
            #TODO:: START STEP1 get and print all event data
            # get all tracker event from events file
            stored_event_data = json.load(event)
            # filter event by condiations
            filter_events_by_medication_organization=list(filter(lambda x:(x["attributeCategoryOptions"],x["orgUnit"])==(medicine_id,org_unit_id),stored_event_data[0]['events']))

            # loop on all met the conditions events to update active and complete dispensed values [ update dispensed values ]
            for dic in filter_events_by_medication_organization:
                # Check if event attribute option equal medication id
                if(dic['attributeCategoryOptions']==medicine_id and dic['orgUnit']==org_unit_id):
                    # Check event active or not
                    if(dic['status']=='ACTIVE'):
                        # loop on all event data values
                        for data_value_loop_one_number in range(len(dic['dataValues'])):
                            # Check if data value has Stock Quantity dispensed
                            if(dic['dataValues'][data_value_loop_one_number]['dataElement']=='LijzB622Z22'):
                                # update active dispense value 
                                active_dispense_value= active_dispense_value + int(dic['dataValues'][data_value_loop_one_number]['value'])
                    # Check event Completed or not
                    elif(dic['status']=='COMPLETED'):
                        # loop on all event data values
                        for data_value_loop_two_number in range(len(dic['dataValues'])):
                                # Check if data value has Stock Quantity dispensed
                                if(dic['dataValues'][data_value_loop_two_number]['dataElement']=='LijzB622Z22'):
                                    # update complete dispense value
                                    complete_dispense_value= complete_dispense_value+int(dic['dataValues'][data_value_loop_two_number]['value'])

            # update quantity before exchange
            quantity_before_exchange=int(dispensed_quantity)-(complete_dispense_value+active_dispense_value)
            print("complete_dispense_value:", complete_dispense_value)
            print("active_dispense_value:", active_dispense_value)
            print("quantity_before_exchange:", quantity_before_exchange)
            
            #TODO:: END STEP1 get and print all event data

            ##TODO:: START STEP2 split every event to different status category

            # Check exchange value if not zero else print zero
            if(quantity_before_exchange>0 or quantity_before_exchange<0):
                # loop on all met the conditions events
                for dic in filter_events_by_medication_organization:
                    # Set variables with default values
                    event_status_active=False
                    not_expired=False
                    event_stock_quantity_dispensed=None
                    event_stock_total=None
                    event_quantity_stock=None
                    # date_for_stock_inventory=datetime.strptime(dic['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date() if dic['eventDate']!=None else ''
                    # Check event status
                    if(dic['status']=='ACTIVE'):
                        event_status_active=True
                    
                    # Loop on all data values
                    for data_value_loop_three_number in range(len(dic['dataValues'])):
                        # Check if event expired or not else not expired
                        if(dic['dataValues'][data_value_loop_three_number]['dataElement']=='xW95VLnIqyP'):
                            event_date_value = datetime.strptime(dic['dataValues'][data_value_loop_three_number]['value'], '%Y-%m-%d').date()
                            event_today_date_value =  datetime.strptime(today.strftime( '%Y-%m-%d'), '%Y-%m-%d').date()
                            if(event_today_date_value<=event_date_value):
                                not_expired=True
                            else:
                                not_expired=False
                        else:
                            not_expired=True
                        
                        # Store event dispensed stock quantity value
                        if(dic['dataValues'][data_value_loop_three_number]['dataElement']=='LijzB622Z22'):
                            event_stock_quantity_dispensed=int(dic['dataValues'][data_value_loop_three_number]['value'])
                        
                        # Store event total stock value
                        if(dic['dataValues'][data_value_loop_three_number]['dataElement']=='bry41dJZ99x'):
                            event_stock_total=int(dic['dataValues'][data_value_loop_three_number]['value'])
                        
                        # Store event stock quantity value
                        if(dic['dataValues'][data_value_loop_three_number]['dataElement']=='eskqGfai0gc'):
                            event_quantity_stock=int(dic['dataValues'][data_value_loop_three_number]['value'])

                    # Check and add to lists        
                    if(event_status_active and not_expired):
                        # print("in")
                        array_for_active_events.append({"event":dic['event'],"date":datetime.strptime(dic['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"stock_quantity_dispensed":event_stock_quantity_dispensed,"stock_total":event_stock_total,"quantity_stock":event_quantity_stock,"query":dic})
                        array_for_negative_values.append({"event":dic['event'],"date":datetime.strptime(dic['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"stock_quantity_dispensed":event_stock_quantity_dispensed,"stock_total":event_stock_total,"quantity_stock":event_quantity_stock,"query":dic})
                    else:
                        # print("out")
                        # check data of stock inventory
                        
                        array_for_not_active_events.append({"event": dic['event'] ,"date":datetime.strptime(dic['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"stock_quantity_dispensed":event_stock_quantity_dispensed,"stock_total":event_stock_total,"quantity_stock":event_quantity_stock,"query":dic})
                        array_for_negative_values.append({"event":dic['event'],"date":datetime.strptime(dic['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"stock_quantity_dispensed":event_stock_quantity_dispensed,"stock_total":event_stock_total,"quantity_stock":event_quantity_stock,"query":dic})



            ##TODO:: END STEP2 

            ###! START STEP3
            print("Start Step 3 ..")
            #? Start Update on DHIS2
            sorted_date_array = sorted(array_for_active_events, key=lambda x: x['date'])
            while quantity_before_exchange!=0:
                print("val"+ str(quantity_before_exchange))
                
            # No Edit Scenario
                if(quantity_before_exchange==0):
                    print("No Edit")
        
            # Positive Scenario
                elif(quantity_before_exchange>0):
                    print("Edit Positive")
                    #? Create New Event
                    if(len(sorted_date_array)==0 and quantity_before_exchange !=0 ):
                        print('number of active event is zero')
                        print(quantity_before_exchange)
                        create_event(org_unit_id,quantity_before_exchange,medicine_id)
                        quantity_before_exchange=0
                        continue

                    #? Update Existed Event
                    elif(len(sorted_date_array)>0):
                        print('>')
                        #sort array by date from old to new
                        for EventJsonArray in range(len(sorted_date_array)):
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
                                print("print else")
                                new_stock_quantity_dispensed=(stock_quantity_dispensed+quantity_before_exchange) # 72+28=100
                                total_quantity=quantity_stock-new_stock_quantity_dispensed
                                new_update_event(medication_id,total_quantity,quantity_stock,new_stock_quantity_dispensed,event_id,organisation_id,program_id,"ACTIVE")
                                quantity_before_exchange=0
                                break
                                
                        
        #?? Negative Scenario
                elif(quantity_before_exchange<0):
                    # print(forNegArray)
                    print("Edit Negative")
                    print(array_for_negative_values)
                    #! Create New Event
                    if(len(array_for_negative_values)==0):
                        print('number of negative event is zero')
                        # create_event(org_unit_id,quantity_before_exchange,medicine_id)
                        quantity_before_exchange=0
                        continue
                    
                    #! Update Exist Event
                    elif(len(array_for_negative_values)>=1):
                        print('>')
                        sorted_date_array = sorted(array_for_negative_values, key=lambda x: x['date'],reverse=True)
                        # print("sorted_date_array",sorted_date_array)
                        for EventJsonArray in range(len(sorted_date_array)):
                            # print("quantity_before_exchange", quantity_before_exchange)
                            if(sorted_date_array[EventJsonArray]['stock_total']==0 and sorted_date_array[EventJsonArray]['stock_quantity_dispensed']==0):
                                print('break == 0')
                                # sorted_date_array.pop(0)
                                continue
                            else:
                                newEventTotal=0
                                if(abs(quantity_before_exchange)>sorted_date_array[EventJsonArray]['stock_quantity_dispensed']):
                                    newEventValue=0
                                    quantity_before_exchange=sorted_date_array[EventJsonArray]['stock_quantity_dispensed']+quantity_before_exchange
                                else:
                                    newEventValue=sorted_date_array[EventJsonArray]['stock_quantity_dispensed']+quantity_before_exchange
                                    quantity_before_exchange=0
                                if(sorted_date_array[EventJsonArray]['stock_total']==None):
                                    sorted_date_array[EventJsonArray]['stock_total']=0
                                if(sorted_date_array[EventJsonArray]['stock_quantity_dispensed']==None):
                                    sorted_date_array[EventJsonArray]['stock_quantity_dispensed']=0
                                updateEventId=sorted_date_array[EventJsonArray]['event']
                                for numberOfDataElement in range(len(sorted_date_array[EventJsonArray]['query']['dataValues'])):
                                    if(sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['dataElement']=='LijzB622Z22'):
                                        sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['value']=newEventValue
                                    if(sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['dataElement']=='LCWyFX0sjqM'):
                                        newEventTotal=sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['value']
                                    if(sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['dataElement']=='bry41dJZ99x'):
                                        sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['value']=newEventTotal-newEventValue
                                #store event it
                                sorted_date_array[EventJsonArray]['query']['status']='ACTIVE'
                                #convert to json
                                toJsonFromEventData=json.dumps(sorted_date_array[EventJsonArray]['query'])
                                eventWithNewData=json.loads(toJsonFromEventData)
                                #TODO!! Check before delete
                                del eventWithNewData["href"]
                                del eventWithNewData['deleted']
                                del eventWithNewData['notes']
                                del eventWithNewData['lastUpdated']
                                del eventWithNewData['eventDate']
                                del eventWithNewData['dueDate']
                                toJsonFormat=json.dumps(eventWithNewData)
                                update_event(updateEventId,toJsonFormat)
                                if(quantity_before_exchange==0 or quantity_before_exchange>0):
                                    print('break')
                                    continue
                                else:
                                    if(len(sorted_date_array)<0):
                                        sorted_date_array.pop(0)
                                    elif(len(sorted_date_array)==0 and quantity_before_exchange < 0):
                                        create_event(org_unit_id,quantity_before_exchange,medicine_id)
                                        quantity_before_exchange=0

                ###! End STEP3
