import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import date
from datetime import datetime
import time
from ..category_options import get_code_data
from ..api import get_org_req,get_tei_org,get_event,get_event_data

def get_org_data(today_date):
    all_array=[]
    # -> Get all org
    get_org_unit_data = json.loads(get_org_req())
    # loop on all org ids
    for data_from_org_unit in range(len(get_org_unit_data['organisationUnits'])):
        org_unit_id = get_org_unit_data['organisationUnits'][data_from_org_unit]['id']
        # --> Get all tei for all org
        get_tei_data = json.loads(get_tei_org(org_unit_id,today_date))
        # check if has data
        if('trackedEntityInstances' in get_tei_data):
            # loop on all tei data
            for number_of_tei in range(len(get_tei_data['trackedEntityInstances'])):
                # store org_tei data to array
                new_data_array_Prescribed = {"tei": "", "program": "","stage":"","orgunit": "", "date": "", 
                        "m1": "", "q1": "", "m2": "","q2": "", "m3": "", "q3": "","m4": "", "q4": "", "m5": "", "q5": "",
                        "m6": "", "q6": "", "m7": "", "q7": "", "m8": "","q8": "", "m9": "","q9": "", "m10": "","q10": "","m11": "","q11": "",
                        "last_update":""}
                new_data_array_Frequently = {"tei": "", "program": "","stage":"","orgunit": "", "date": "",
                        "m1": "", "q1": "", "m2": "","q2": "", "m3": "", "q3": "","m4": "", "q4": "", "m5": "", "q5": "",
                        "m6": "", "q6": "", "m7": "", "q7": "", "m8": "","q8": "", "m9": "","q9": "", "m10": "","q10": "",
                        "m11": "","q11": "", "m12": "","q12": "", "m13": "","q13": "","m14": "","q14": "",
                        "last_update":""}
                tei_id = get_tei_data['trackedEntityInstances'][number_of_tei]['trackedEntityInstance']
                # new_data_array['tei'] = tei_id
                # # ---> Get all event for every tei
                event_data = json.loads(get_event(tei_id,today_date))
                for number_of_event in range(len(event_data['events'])):
                    event_id = event_data['events'][number_of_event]['event']
                    orgunit = event_data['events'][number_of_event]['orgUnit']
                    # ----> Get all data for every event
                    get_event_id_data = json.loads(get_event_data(event_id))
                    if('dataValues' in json.dumps(get_event_id_data)):
                        program_stage_type=get_event_id_data['programStage']
                        program_id=event_data['events'][number_of_event]['program']
                        if(program_stage_type=="JV6n7FhC7xp"):
                            new_data_array_Prescribed['tei']=tei_id
                            new_data_array_Prescribed['program']=program_id
                            new_data_array_Prescribed['stage']=program_stage_type
                            new_data_array_Prescribed['orgunit']=orgunit
                            new_data_array_Prescribed['date'] = str(datetime.strptime(get_event_id_data['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date())
                            new_data_array_Prescribed['last_update'] = str(datetime.strptime(get_event_id_data['dueDate'], '%Y-%m-%dT%H:%M:%S.%f').date())
                            for numberOfDataValue in range(len(get_event_id_data['dataValues'])):
                                event_id_data = get_event_id_data['dataValues'][numberOfDataValue]['dataElement']
                                if event_id_data == "aM2Vn0UUPJB":
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m1'] = get_code_data(event_value)
                                if event_id_data == "WSeukMBwbQ3":
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m2'] = get_code_data(event_value)
                                if event_id_data == "TORfS27wR0q":
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m3'] = get_code_data(event_value)
                                if event_id_data == "TnrWDEL4PoR":
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m4'] = get_code_data(event_value)
                                if event_id_data == "iy166uomfXk":
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m5'] = get_code_data(event_value)
                                if event_id_data == "ntECq4xEo24":
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m6'] = get_code_data(event_value)
                                if event_id_data == "Ne2veOUhPw0":
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m7'] = get_code_data(event_value)
                                if event_id_data == "R2rxr1Z8i4v":
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m8'] = get_code_data(event_value)
                                if event_id_data == "Dlx79ePwf1g":
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m9'] = get_code_data(event_value)
                                if event_id_data == "oTCRn8enMzd":
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m10'] = get_code_data(event_value)
                                if event_id_data == "nTd67mb0PJe":
                                    event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                                    new_data_array_Prescribed['m11'] = get_code_data(event_value)
                                # Check Quantity
                                if event_id_data == "HS5mppnnRUD":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q1'] = event_value
                                if event_id_data == "Kzxa8SKjCdp":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q2'] = event_value
                                if event_id_data == "wmkND48fkvf":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q3'] = event_value
                                if event_id_data == "sm78nae74E0":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q4'] = event_value
                                if event_id_data == "YR7bARfLBay":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q5'] = event_value
                                if event_id_data == "Pl3jCeEVYVG":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q6'] = event_value
                                if event_id_data == "J6s8Ju9Y1xk":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q7'] = event_value
                                if event_id_data == "xFAUNJilvDg":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q8'] = event_value
                                if event_id_data == "tn3XjDR6aUt":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q9'] = event_value
                                if event_id_data == "H2g1tcKI0sK":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q10'] = event_value
                                if event_id_data == "wFeFcxSnOO0":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Prescribed['q11'] = event_value

                            #TODO::insert To Database
                            # print(new_data_array_Prescribed['tei'] == "")
                            # print(new_data_array_Prescribed)
                            all_array.append(new_data_array_Prescribed)

                        if(program_stage_type=="tJQ1UCpkCy2"):
                            new_data_array_Frequently['tei']=tei_id
                            new_data_array_Frequently['program']=program_id
                            new_data_array_Frequently['stage']=program_stage_type
                            new_data_array_Frequently['orgunit']=orgunit
                            new_data_array_Frequently['date'] = str(datetime.strptime(get_event_id_data['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date())
                            new_data_array_Frequently['last_update'] = str(datetime.strptime(get_event_id_data['dueDate'], '%Y-%m-%dT%H:%M:%S.%f').date())
                            for numberOfDataValue in range(len(get_event_id_data['dataValues'])):
                                event_id_data = get_event_id_data['dataValues'][numberOfDataValue]['dataElement']                                
                                if event_id_data == "g3jYfDWMlju":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m1'] = get_code_data("M-301-1001")
                                if event_id_data == "ezwWMPb12eO":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m2'] = get_code_data("M-123-1004")
                                if event_id_data == "iifVrszTRRz":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m3'] =  get_code_data("M-123-1018")
                                if event_id_data == "KIZvcIfQvpT":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m4'] = get_code_data("M-192-1010")
                                if event_id_data == "qs0I9NsfUxu":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m5'] = get_code_data("M-192-1035")
                                if event_id_data == "YxFGAkRihhj":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m6'] =  get_code_data("M-123-1030")
                                if event_id_data == "x2qkkLksG0N":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m7'] = get_code_data("M-123-1035")
                                if event_id_data == "uuaO52vR7Sc":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m8'] = get_code_data("M-192-1016")
                                if event_id_data == "cgKw0UiSSzA":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m9'] =  get_code_data("M-192-1012")
                                if event_id_data == "A0WmBW0xr3Q":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m10'] =  get_code_data("M-121-1020")
                                if event_id_data == "igbaI5cMEch":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m11'] = get_code_data("M-123-1041")
                                if event_id_data == "tXnR137oYs6":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m12'] =  get_code_data("M-251-4012")
                                if event_id_data == "joyfXYlQ0aS":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m13'] =  get_code_data("M-251-4013")
                                if event_id_data == "Oh5NachZvua":
                                    if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                        new_data_array_Frequently['m14'] =  get_code_data("M-181-1018")
                                if event_id_data == "gTreHa9FsAJ":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q1'] = event_value
                                if event_id_data == "nubIuNPn6kP":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q2'] = event_value
                                if event_id_data == "UOVMe9Hftr8":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q3'] = event_value
                                if event_id_data == "cMVX1z75Uvh":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q4'] = event_value
                                if event_id_data == "B3rbznpTyjJ":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q5'] = event_value
                                if event_id_data == "nxfbinD79RB":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q6'] = event_value    
                                if event_id_data == "BIP1buozD2e":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q7'] = event_value
                                if event_id_data == "xGxzPWNaSuz":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q8'] = event_value
                                if event_id_data == "Fe9k17OVHPe":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q9'] = event_value     
                                if event_id_data == "wiLMg4LNV3V":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q10'] = event_value     
                                if event_id_data == "z8F0ZEgFeeY":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q11'] = event_value     
                                if event_id_data == "btTycEIdfBr":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q12'] = event_value     
                                if event_id_data == "vO16pLLv3u8":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q13'] = event_value     
                                if event_id_data == "mIKc81UxFte":
                                    event_value = int(
                                        get_event_id_data['dataValues'][numberOfDataValue]['value'])
                                    new_data_array_Frequently['q14'] = event_value 
                             #TODO::insert To Database
                            # print(new_data_array_Frequently)
                            all_array.append(new_data_array_Frequently)
    #return all event data                    
    return all_array                   


