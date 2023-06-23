# Define get organisation data to retrieve all event from all organisation by tei
from requests.auth import HTTPBasicAuth
import json
from datetime import date
from datetime import datetime
from ..category_options import get_code_data
from ..api import get_org_req, get_tei_org, get_event, get_event_data
from config import *
# This function make multi loop to get all event data from all organisation for every tei and return array of event objects


def get_org_data(max_Number_Of_Loop):
    """
    Retrieves prescribed medication data from multiple sources and returns a list of event objects.

    Args:
        max_Number_Of_Loop (int): The maximum number of loops to perform.

    Returns:
        list: A list of event objects containing prescribed medication data.

    Overview:
    This function retrieves data from different sources including organization units, tracked entity instances,
    and events. It iterates over the retrieved data and extracts prescribed medication information for each event.
    The extracted data is stored in event objects and added to a list. Finally, the function returns the list of
    event objects.

    Note:
    - The commented-out code blocks and unused variables do not affect the functionality of the function.
    - The max_Number_Of_Loop parameter is currently not utilized in the function.
    """
    all_array = []
    array_number_loop=0
    # Get all org
    get_org_unit_data = json.loads(get_org_req())
    # loop on all org ids
    for data_from_org_unit in range(len(get_org_unit_data['organisationUnits'])):
        org_unit_id = get_org_unit_data['organisationUnits'][data_from_org_unit]['id']
        # Get all tei for all org
        get_tei_data = json.loads(get_tei_org(
            org_unit_id, first_day, last_day))

        # check if has data
        if('trackedEntityInstances' in get_tei_data):
            array_number_loop+=1
            # loop on all tei data
            for number_of_tei in range(len(get_tei_data['trackedEntityInstances'])):
                # store org_tei data to array
                tei_id = get_tei_data['trackedEntityInstances'][number_of_tei]
                # Get all event for every tei
                event_data = json.loads(get_event(tei_id))
                for number_of_event in range(len(event_data['events'])):
                    # create prescribed empty template object
                    new_data_array_Prescribed = {"event_id": "", "tei": "", "program": "", "stage": "", "orgunit": "", "date": "",
                                                 "m1": "", "q1": "", "m2": "", "q2": "", "m3": "", "q3": "", "m4": "", "q4": "", "m5": "", "q5": "",
                                                 "m6": "", "q6": "", "m7": "", "q7": "", "m8": "", "q8": "", "m9": "", "q9": "", "m10": "", "q10": "", "m11": "", "q11": "",
                                                 "last_update": ""}
                    # define event id and organisation id variable
                    event_id = event_data['events'][number_of_event]['event']
                    organisation_id = event_data['events'][number_of_event]['orgUnit']
                    # Get all data for every event
                    get_event_id_data = json.loads(get_event_data(event_id))
                    if('dataValues' in json.dumps(get_event_id_data)):
                        program_stage_type = get_event_id_data['programStage']
                        program_id = event_data['events'][number_of_event]['program']
                        # Check if stage type prescribed
                        if(program_stage_type == stageForPrescribedMedications):
                            new_data_array_Prescribed['event_id'] = event_id
                            new_data_array_Prescribed['tei'] = tei_id
                            new_data_array_Prescribed['program'] = program_id
                            new_data_array_Prescribed['stage'] = program_stage_type
                            new_data_array_Prescribed['orgunit'] = organisation_id
                            try:
                                new_data_array_Prescribed['date'] = str(datetime.strptime(
                                    get_event_id_data['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date())
                            except:
                                new_data_array_Prescribed['date'] = None
                            try:
                                new_data_array_Prescribed['last_update'] = str(datetime.strptime(
                                    get_event_id_data['dueDate'], '%Y-%m-%dT%H:%M:%S.%f').date())
                            except:
                                new_data_array_Prescribed['last_update'] = None

                            for numberOfDataValue in range(len(get_event_id_data['dataValues'])):
                                event_id_data = get_event_id_data['dataValues'][numberOfDataValue]['dataElement']
                                # Check Prescribed Medication
                                if event_id_data == Pharm_Medicine_Name:
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m1'] = get_code_data(
                                        event_value)
                                if event_id_data == Pharm_Medicine_Name_1:
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m2'] = get_code_data(
                                        event_value)
                                if event_id_data == Pharm_Medicine_Name_2:
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m3'] = get_code_data(
                                        event_value)
                                if event_id_data == Pharm_Medicine_Name_3:
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m4'] = get_code_data(
                                        event_value)
                                if event_id_data == Pharm_Medicine_Name_4:
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m5'] = get_code_data(
                                        event_value)
                                if event_id_data == Pharm_Medicine_Name_5:
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m6'] = get_code_data(
                                        event_value)
                                if event_id_data == Pharm_Medicine_Name_6:
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m7'] = get_code_data(
                                        event_value)
                                if event_id_data == Pharm_Medicine_Name_7:
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m8'] = get_code_data(
                                        event_value)
                                if event_id_data == Pharm_Medicine_Name_8:
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m9'] = get_code_data(
                                        event_value)
                                if event_id_data == Pharm_Medicine_Name_9:
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m10'] = get_code_data(
                                        event_value)
                                if event_id_data == Pharm_Medicine_Name_10:
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m11'] = get_code_data(
                                        event_value)
                                # Check Prescribed Quantity
                                if event_id_data == Pharmacy_QTY_Despensed:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q1'] = event_value
                                if event_id_data == Pharmacy_QTY_Despensed_1:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q2'] = event_value
                                if event_id_data == Pharmacy_QTY_Despensed_2:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q3'] = event_value
                                if event_id_data == Pharmacy_QTY_Despensed_3:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q4'] = event_value
                                if event_id_data == Pharmacy_QTY_Despensed_4:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q5'] = event_value
                                if event_id_data == Pharmacy_QTY_Despensed_5:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q6'] = event_value
                                if event_id_data == Pharmacy_QTY_Despensed_6:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q7'] = event_value
                                if event_id_data == Pharmacy_QTY_Despensed_7:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q8'] = event_value
                                if event_id_data == Pharmacy_QTY_Despensed_8:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q9'] = event_value
                                if event_id_data == Pharmacy_QTY_Despensed_9:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q10'] = event_value
                                if event_id_data == Pharmacy_QTY_Despensed_10:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q11'] = event_value

                            # Add prescribed array to all_array variable
                            all_array.append(new_data_array_Prescribed)

        # if(array_number_loop>max_Number_Of_Loop):
        #     break
    # return all event objects
    return all_array
