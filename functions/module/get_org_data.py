# Define get organisation data to retrieve all event from all organisation by tei
from requests.auth import HTTPBasicAuth
import json
from datetime import date
from datetime import datetime
from ..category_options import get_code_data
from ..api import get_org_req, get_tei_org, get_event, get_event_data
from config import *
# This function make multi loop to get all event data from all organisation for every tei and return array of event objects


def get_org_data():
    all_array = []
    # Get all org
    get_org_unit_data = json.loads(get_org_req())
    # loop on all org ids
    for data_from_org_unit in range(len(get_org_unit_data['organisationUnits'])):
        org_unit_id = get_org_unit_data['organisationUnits'][data_from_org_unit]['id']
        # print("org_unit_id:",org_unit_id)
        # Get all tei for all org
        get_tei_data = json.loads(get_tei_org(
            org_unit_id, first_day, last_day))
        # check if has data
        if('trackedEntityInstances' in get_tei_data):
            # loop on all tei data
            for number_of_tei in range(len(get_tei_data['trackedEntityInstances'])):
                # store org_tei data to array
                tei_id = get_tei_data['trackedEntityInstances'][number_of_tei]['trackedEntityInstance']
                # print("tei_id:",tei_id)
                # Get all event for every tei
                event_data = json.loads(get_event(tei_id))
                for number_of_event in range(len(event_data['events'])):
                    # create prescribed empty template object
                    new_data_array_Prescribed = {"event_id": "", "tei": "", "program": "", "stage": "", "orgunit": "", "date": "",
                                                 "m1": "", "q1": "", "m2": "", "q2": "", "m3": "", "q3": "", "m4": "", "q4": "", "m5": "", "q5": "",
                                                 "m6": "", "q6": "", "m7": "", "q7": "", "m8": "", "q8": "", "m9": "", "q9": "", "m10": "", "q10": "", "m11": "", "q11": "",
                                                 "last_update": ""}
                    # create frequently empty template object
                    new_data_array_Frequently = {"event_id": "", "tei": "", "program": "", "stage": "", "orgunit": "", "date": "",
                                                 "m1": "", "q1": "", "m2": "", "q2": "", "m3": "", "q3": "", "m4": "", "q4": "", "m5": "", "q5": "",
                                                 "m6": "", "q6": "", "m7": "", "q7": "", "m8": "", "q8": "", "m9": "", "q9": "", "m10": "", "q10": "",
                                                 "m11": "", "q11": "", "m12": "", "q12": "", "m13": "", "q13": "", "m14": "", "q14": "", "m15": "", "q15": "",
                                                 "last_update": ""}
                    # define event id and organisation id variable
                    event_id = event_data['events'][number_of_event]['event']
                    # print("event_id:",event_id)
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
                                new_data_array_Prescribed['last_update'] = None
                            try:
                                new_data_array_Prescribed['last_update'] = str(datetime.strptime(
                                    get_event_id_data['dueDate'], '%Y-%m-%dT%H:%M:%S.%f').date())
                            except:
                                new_data_array_Prescribed['date'] = None
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

                        # Check if stage type frequently
                        if(program_stage_type == stageForFrequentlyMedications):
                            # store all event data on frequently object
                            new_data_array_Frequently['event_id'] = event_id
                            new_data_array_Frequently['tei'] = tei_id
                            new_data_array_Frequently['program'] = program_id
                            new_data_array_Frequently['stage'] = program_stage_type
                            new_data_array_Frequently['orgunit'] = organisation_id
                            try:
                                new_data_array_Frequently['date'] = str(datetime.strptime(
                                    get_event_id_data['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date())
                            except:
                                new_data_array_Frequently['date'] = None
                            try:
                                new_data_array_Frequently['last_update'] = str(datetime.strptime(
                                    get_event_id_data['dueDate'], '%Y-%m-%dT%H:%M:%S.%f').date())
                            except:
                                new_data_array_Frequently['last_update'] = None
                            for numberOfDataValue in range(len(get_event_id_data['dataValues'])):
                                event_id_data = get_event_id_data['dataValues'][numberOfDataValue]['dataElement']
                                # Check Frequently Medication
                                # 1
                                if event_id_data == Pharmacy_Frequently_Order_Atorvastatin:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m1'] = get_code_data(
                                            Pharmacy_Frequently_Order_Atorvastatin_code)
                                # 2
                                if event_id_data == Pharmacy_Frequently_Order_AMLODIPINE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m2'] = get_code_data(
                                            Pharmacy_Frequently_Order_AMLODIPINE_code)
                                # 3
                                if event_id_data == Pharmacy_Frequently_Order_BISOPROLOL:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m3'] = get_code_data(
                                            Pharmacy_Frequently_Order_BISOPROLOL_code)
                                # 4
                                if event_id_data == Pharmacy_Frequently_Order_METFORMIN:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m4'] = get_code_data(
                                            Pharmacy_Frequently_Order_METFORMIN_code)
                                # 5
                                if event_id_data == Pharmacy_Frequently_Order_SITAGLIPTIN:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m5'] = get_code_data(
                                            Pharmacy_Frequently_Order_SITAGLIPTIN_code)
                                # 6
                                if event_id_data == Pharmacy_Frequently_Order_ENALAPRIL20:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m6'] = get_code_data(
                                            Pharmacy_Frequently_Order_ENALAPRIL20_code)
                                # 7
                                if event_id_data == Pharmacy_Frequently_Order_ENALAPRIL5:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m7'] = get_code_data(
                                            Pharmacy_Frequently_Order_ENALAPRIL5_code)
                                # 8
                                if event_id_data == Pharmacy_Frequently_Order_glimepiride4:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m8'] = get_code_data(
                                            Pharmacy_Frequently_Order_glimepiride4_code)
                                # 9
                                if event_id_data == Pharmacy_Frequently_Order_glimepiride2:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m9'] = get_code_data(
                                            Pharmacy_Frequently_Order_glimepiride2_code)
                                # 10
                                if event_id_data == Pharmacy_Frequently_Order_ISOSORBIDE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m10'] = get_code_data(
                                            Pharmacy_Frequently_Order_ISOSORBIDE_code)
                                # 11
                                if event_id_data == Pharmacy_Frequently_Order_losartan:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m11'] = get_code_data(
                                            Pharmacy_Frequently_Order_losartan_code)
                                # 12
                                if event_id_data == Pharmacy_Frequently_Order_SALBUTAMOL:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m12'] = get_code_data(
                                            Pharmacy_Frequently_Order_SALBUTAMOL_code)
                                # 13
                                if event_id_data == Pharmacy_Frequently_Order_ipratropium:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m13'] = get_code_data(
                                            Pharmacy_Frequently_Order_ipratropium_code)
                                # 14
                                if event_id_data == Pharmacy_Frequently_Order_OMEPRAZOLE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m14'] = get_code_data(
                                            Pharmacy_Frequently_Order_OMEPRAZOLE_code)
                                # 15
                                if event_id_data == Pharmacy_Frequently_Order_ASA100:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m15'] = get_code_data(
                                            Pharmacy_Frequently_Order_ASA100_code)
                                # 16
                                if event_id_data == Pharmacy_Frequently_Order_ALLOPURINOL:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m16'] = get_code_data(
                                            Pharmacy_Frequently_Order_ALLOPURINOL_code)
                                # 17
                                if event_id_data == Pharmacy_Frequently_Order_ATENOLOL:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m17'] = get_code_data(
                                            Pharmacy_Frequently_Order_ATENOLOL_code)
                                # 18
                                if event_id_data == Pharmacy_Frequently_Order_atenolol25:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m18'] = get_code_data(
                                            Pharmacy_Frequently_Order_atenolol25_code)
                                # 19
                                if event_id_data == Pharmacy_Frequently_Order_BETAHISTINE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m19'] = get_code_data(
                                            Pharmacy_Frequently_Order_BETAHISTINE_code)
                                # 20
                                if event_id_data == Pharmacy_Frequently_Order_CALCIUM:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m20'] = get_code_data(
                                            Pharmacy_Frequently_Order_CALCIUM_code)
                                # 21
                                if event_id_data == Pharmacy_Frequently_Order_spiranolactone:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m21'] = get_code_data(
                                            Pharmacy_Frequently_Order_spiranolactone_code)
                                # 22
                                if event_id_data == Pharmacy_Frequently_Order_SPIRONOLACTONE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m22'] = get_code_data(
                                            Pharmacy_Frequently_Order_SPIRONOLACTONE_code)
                                # 23
                                if event_id_data == Pharmacy_Frequently_Order_ALFACALCIDOL:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m23'] = get_code_data(
                                            Pharmacy_Frequently_Order_ALFACALCIDOL_code)
                                # 24
                                if event_id_data == Pharmacy_Frequently_Order_FERROUS:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m24'] = get_code_data(
                                            Pharmacy_Frequently_Order_FERROUS_code)
                                # 25
                                if event_id_data == Pharmacy_Frequently_Order_FUROSEMIDE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m25'] = get_code_data(
                                            Pharmacy_Frequently_Order_FUROSEMIDE_code)
                                # 26
                                if event_id_data == Pharmacy_Frequently_Order_METHOTREXATE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m26'] = get_code_data(
                                            Pharmacy_Frequently_Order_METHOTREXATE_code)
                                # 27
                                if event_id_data == Pharmacy_Frequently_Order_DOXAZOCIN:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m27'] = get_code_data(
                                            Pharmacy_Frequently_Order_DOXAZOCIN_code)
                                # 28
                                if event_id_data == Pharmacy_Frequently_Order_PREDNISOLONE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m28'] = get_code_data(
                                            Pharmacy_Frequently_Order_PREDNISOLONE_code)
                                # 29
                                if event_id_data == Pharmacy_Frequently_Order_PREDNISOLONE5:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m29'] = get_code_data(
                                            Pharmacy_Frequently_Order_PREDNISOLONE5_code)
                                # 30
                                if event_id_data == Pharmacy_Frequently_Order_HYDROCHLORTHIAZIDE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m30'] = get_code_data(
                                            Pharmacy_Frequently_Order_HYDROCHLORTHIAZIDE_code)   
                                # 31
                                if event_id_data == Pharmacy_Frequently_Order_thyroxine50:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m31'] = get_code_data(
                                            Pharmacy_Frequently_Order_thyroxine50_code)                               
                                # 32
                                if event_id_data == Pharmacy_Frequently_Order_THYROXINE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m32'] = get_code_data(
                                            Pharmacy_Frequently_Order_THYROXINE_code)                               
                                # 33
                                if event_id_data == Pharmacy_Frequently_Order_clopidogrel:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m33'] = get_code_data(
                                            Pharmacy_Frequently_Order_clopidogrel_code)                                
                                # 34
                                if event_id_data == Pharmacy_Frequently_Order_sitaGLIPTIN:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m34'] = get_code_data(
                                            Pharmacy_Frequently_Order_sitaGLIPTIN_code)                                
                                # 35
                                if event_id_data == Pharmacy_Frequently_Order_INSULIN:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m35'] = get_code_data(
                                            Pharmacy_Frequently_Order_INSULIN_code)                                
                                # 36
                                if event_id_data == Pharmacy_Frequently_Order_GLARGINE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m36'] = get_code_data(
                                            Pharmacy_Frequently_Order_GLARGINE_code)                               
                                # 37
                                if event_id_data == Pharmacy_Frequently_Order_DETEMIR:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m37'] = get_code_data(
                                            Pharmacy_Frequently_Order_DETEMIR_code)                                
                                # 38
                                if event_id_data == Pharmacy_Frequently_Order_INSULIN_NPH:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m38'] = get_code_data(
                                            Pharmacy_Frequently_Order_INSULIN_NPH_code)                               
                                # 39
                                if event_id_data == Pharmacy_Frequently_Order_INSULIN_ACT:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m39'] = get_code_data(
                                            Pharmacy_Frequently_Order_INSULIN_ACT_code)                               
                                # 40
                                if event_id_data == Pharmacy_Frequently_Order_LISPRO:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m40'] = get_code_data(
                                            Pharmacy_Frequently_Order_LISPRO_code)                                
                                # 41
                                if event_id_data == Pharmacy_Frequently_Order_GLULISINE:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m41'] = get_code_data(
                                            Pharmacy_Frequently_Order_GLULISINE_code)                               
                                # 42
                                if event_id_data == Pharmacy_Frequently_Order_ASPART:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m42'] = get_code_data(
                                            Pharmacy_Frequently_Order_ASPART_code)                              
                                # 43
                                if event_id_data == Pharmacy_Frequently_Order_Famotidine:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m43'] = get_code_data(
                                            Pharmacy_Frequently_Order_Famotidine_code)                               
                                # 44
                                if event_id_data == Pharmacy_Frequently_Order_Famotidine40:
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m44'] = get_code_data(
                                            Pharmacy_Frequently_Order_Famotidine40_code)                               
                 

                                # Check Frequently Quantity
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_1:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q1'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_2:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q2'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_3:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q3'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_4:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q4'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_5:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q5'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_6:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q6'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_7:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q7'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_8:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q8'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_9:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q9'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_10:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q10'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_11:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q11'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_12:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q12'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_13:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q13'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_14:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q14'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_15:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q15'] = event_value

                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_16:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q16'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_17:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q17'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_18:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q18'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_19:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q19'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_20:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q20'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_21:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q21'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_22:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q22'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_23:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q23'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_24:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q24'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_25:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q25'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_26:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q26'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_27:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q27'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_28:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q28'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_29:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q29'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_30:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q30'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_31:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q31'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_32:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q32'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_33:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q33'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_34:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q34'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_35:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q35'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_36:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q36'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_37:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q37'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_38:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q38'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_39:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q39'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_40:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q40'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_41:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q41'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_42:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q42'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_43:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q43'] = event_value
                                if event_id_data == Pharmacy_FrequentlyMedication_Despensed_44:
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q44'] = event_value







                            # Add frequently array to all_array variable
                            all_array.append(new_data_array_Frequently)
    # return all event objects
    return all_array
