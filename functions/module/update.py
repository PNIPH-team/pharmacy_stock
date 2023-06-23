# Define all type of action to reverse it to dhis2 system (capture)
import json
from functions.module.split_events import split_events
from functions.module.update_scenario import update_scenario
from functions.files import return_path
from config import dataElementForQuantity
# This function work to check every new event with existing event on capture program
def updateData(all_event_data_groupby_json):
    """
    Updates data based on the provided event data.

    Args:
        all_event_data_groupby_json (str): JSON string containing the event data.

    Returns:
        None
    """
    #Load last updated list from database
    group_by_database_array=json.loads(all_event_data_groupby_json)
    for group_by_database_list in range(len(group_by_database_array)):

        #define variables from database data
        org_unit_id=group_by_database_array[group_by_database_list]['orgunit_id']
        medicine_id=group_by_database_array[group_by_database_list]['medication_code']
        dispensed_quantity=group_by_database_array[group_by_database_list]['medication_total_quantity']
        complete_dispense_value=0
        active_dispense_value=0

        # read events data from json file
        with open(return_path()+'/data/events.json') as event:
            # GET List of event for the same id
            #? START STEP1 get and store all event data
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
                            if(dic['dataValues'][data_value_loop_one_number]['dataElement']==dataElementForQuantity):
                                # update active dispense value 
                                active_dispense_value= active_dispense_value + int(dic['dataValues'][data_value_loop_one_number]['value'])
                    # Check event Completed or not
                    elif(dic['status']=='COMPLETED'):
                        # loop on all event data values
                        for data_value_loop_two_number in range(len(dic['dataValues'])):
                                # Check if data value has Stock Quantity dispensed
                                if(dic['dataValues'][data_value_loop_two_number]['dataElement']==dataElementForQuantity):
                                    # update complete dispense value
                                    complete_dispense_value= complete_dispense_value+int(dic['dataValues'][data_value_loop_two_number]['value'])

            # update quantity before exchange
            quantity_before_exchange=int(dispensed_quantity)-(complete_dispense_value+active_dispense_value)
            
            ##? START STEP2 split every event to different status category
            array_for_active_events,array_for_not_active_events,array_for_negative_values=split_events(quantity_before_exchange,filter_events_by_medication_organization)
            ##? START STEP3 Start Update on DHIS2
            update_scenario(quantity_before_exchange,array_for_active_events,array_for_negative_values,org_unit_id,medicine_id)

