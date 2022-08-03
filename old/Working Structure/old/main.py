# Import Library
import json
import pandas as pd
import requests
import os
import mysql.connector
from mysql.connector import Error
from requests.auth import HTTPBasicAuth
from datetime import date
from datetime import datetime

#connect with mysql
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='stock',
                                         user='root',
                                         port=8889,
                                         password='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
except Error as e:
    print("Error while connecting to MySQL", e)

# Define Functions and Some Variables
categoryOptionsList = []
today = date.today()
newest_data = []
Start_DateTime = datetime.now()
print("Start At: ", Start_DateTime)
today_date = today.strftime("%Y-%m-%d")
todayDateTime = "LOG/Stock_" + str(datetime.now())
path = '/Users/salehabbas/Developer/Python/pharmacy_stock/' + todayDateTime
try:
    os.mkdir(path)
except OSError as error:
    print(error)
def writefile(FileName, Data):
    json_data = json.dumps(Data, ensure_ascii=False)
    file = open(FileName, "w")
    with open(file.name, "w") as files:
        files.write(json_data)
    file.close()
def category_options():
    category_options_req = requests.get(
        "https://hmis.moh.ps/tr-dev/api/categoryOptions?fields=id,code",
        auth=HTTPBasicAuth('Saleh', 'Test@123')).json()
    store_category(category_options_req["categoryOptions"])
    while category_options_req["pager"]['pageCount'] != category_options_req["pager"]['page']:
        # ? print(categoryOptions_req["pager"]['nextPage'])
        category_options_req = requests.get(
            category_options_req["pager"]['nextPage'], auth=HTTPBasicAuth('Saleh', 'Test@123')).json()
        store_category(category_options_req["categoryOptions"])
    writefile("categoryOptions.json", categoryOptionsList)
def store_category(args):
    for category_data in args:
        categoryOptionsList.append(category_data)
def check(args):
    if(args=='' or args==None):
        return None
    else:
        return args
print("--------------------------------Mapping And Store attributeCategoryOptions--------------------------------")
def MappingData():
    NewMappingArray = []
    with open('categoryOptions.json') as categoryOptionsFile, open(todayDateTime + "/GroupData_" + today_date + ".json") as GroupDataFile:
        catFile = json.load(categoryOptionsFile)
        groupFile = json.load(GroupDataFile)
        for dataFromGroup in range(len(groupFile['data'])):
            mCode = ""
            OrgUnit_fromjson = groupFile['data'][dataFromGroup]['orgunit']
            quantity_fromjson = groupFile['data'][dataFromGroup]['q']
            mName = groupFile['data'][dataFromGroup]['m']
            for dataFromCategory in range(len(catFile)):
                if catFile[dataFromCategory]['code'] == mName:
                    mCode = catFile[dataFromCategory]['id']
                    newArray = {"orgunit": OrgUnit_fromjson,
                                "mCode": mCode, "quantity": quantity_fromjson}
                    NewMappingArray.append(newArray)
        if len(groupFile['data']) != len(NewMappingArray):
            category_options()
            MappingData()
        else:
            jsonArrayMapping = json.dumps(NewMappingArray)
            MappingDataArray = json.loads(jsonArrayMapping)
            writefile(todayDateTime + "/GroupData_Mapping_" + today_date +
                      ".json", MappingDataArray)
    return MappingDataArray
if not os.path.exists('categoryOptions.json'):
    category_options()

# Get Data From DHIS2
print("--------------------------------Start Loop------------------------")
    #! 1) Get All Org Unit
get_org_unit_req = requests.get(
    "https://hmis.moh.ps/tr-dev/api/programs/fnIEoaflGxX?fields=organisationUnits",
    auth=HTTPBasicAuth('Saleh', 'Test@123'))
get_org_unit_data = json.loads(get_org_unit_req.text)
for dataFromOrgUnit in range(len(get_org_unit_data['organisationUnits'])):
    org_unit_id = get_org_unit_data['organisationUnits'][dataFromOrgUnit]['id']
    # print(get_org_unit_data['organisationUnits'][u]['id'])
    # ! 2) Get all TEI For This orgUnit
    get_tei = requests.get(
        "https://hmis.moh.ps/tr-dev/api/trackedEntityInstances?ou=" +
        org_unit_id+"&fields=trackedEntityInstance&lastUpdatedEndDate="
        + today_date + "&lastUpdatedStartDate=" + today_date,
        auth=HTTPBasicAuth('Saleh', 'Test@123'))
    get_tei_data = json.loads(get_tei.text)
    for numberOfTEI in range(len(get_tei_data['trackedEntityInstances'])):
        #? Store All Data into array
        loop_array = {"tei": "", "program": "", "orgunit": "", "date": "", "m": "", "q": "", "m1": "", "q1": "", "m2": "",
                   "q2": "", "m3": "", "q3": "",
                   "m4": "", "q4": "", "m5": "", "q5": "", "m6": "", "q6": "", "m7": "", "q7": "", "m8": "",
                   "q8": "", "m9": "", "q9": "", "m10": "", "q10": ""
                   , "m11": "", "q11": "", "m12": "",
                   "q12": "", "m13": "", "q13": "",
                   "m14": "", "q14": "", "m15": "", "q15": "", "m16": "", "q16": "", "m17": "", "q17": "", "m18": "",
                   "q18": "", "m19": "", "q19": "", "m20": "", "q20": "", "m21": "", "q21": "", "m22": "",
                   "q22": "", "m23": "", "q23": "", "m24": "", "q24": "","last_update":""}
        tei_id = get_tei_data['trackedEntityInstances'][numberOfTEI]['trackedEntityInstance']
        loop_array['tei'] = tei_id
    #! 3) Get all event And orgUnit For This TEI
        get_event = requests.get(
            "https://hmis.moh.ps/tr-dev/api/events?trackedEntityInstance=" + tei_id + "&lastUpdatedEndDate=" +
            today_date + "&lastUpdatedStartDate=" + today_date + "&fields=event,orgUnit,program",
            auth=HTTPBasicAuth('Saleh', 'Test@123'))
        get_event_data = json.loads(get_event.text)
        for numberOfEvent in range(len(get_event_data['events'])):
            event_id = get_event_data['events'][numberOfEvent]['event']
            orgunit = get_event_data['events'][numberOfEvent]['orgUnit']
            loop_array['program'] = get_event_data['events'][numberOfEvent]['program']
            loop_array['orgunit'] = orgunit
    #! 4) Get each event Data
            get_event_id = requests.get(
                "https://hmis.moh.ps/tr-dev/api/events/" + event_id, auth=HTTPBasicAuth('Saleh', 'Test@123'))
            get_event_id_data = json.loads(get_event_id.text)
            loop_array['date'] = str(get_event_id_data['eventDate'])
            loop_array['last_update'] = str(get_event_id_data['dueDate'])
            #? Store all variables into array
            if('dataValues' in json.dumps(get_event_id_data)):
                for numberOfDataValue in range(len(get_event_id_data['dataValues'])):
                    loop_array['program'] = event_id
                    event_id_data = get_event_id_data['dataValues'][numberOfDataValue]['dataElement']
                    if event_id_data == "aM2Vn0UUPJB":
                        event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                        loop_array['m'] = event_value
                    if event_id_data == "WSeukMBwbQ3":
                        event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                        loop_array['m1'] = event_value
                    if event_id_data == "TORfS27wR0q":
                        event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                        loop_array['m2'] = event_value
                    if event_id_data == "TnrWDEL4PoR":
                        event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                        loop_array['m3'] = event_value
                    if event_id_data == "iy166uomfXk":
                        event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                        loop_array['m4'] = event_value
                    if event_id_data == "ntECq4xEo24":
                        event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                        loop_array['m5'] = event_value
                    if event_id_data == "Ne2veOUhPw0":
                        event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                        loop_array['m6'] = event_value
                    if event_id_data == "R2rxr1Z8i4v":
                        event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                        loop_array['m7'] = event_value
                    if event_id_data == "Dlx79ePwf1g":
                        event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                        loop_array['m8'] = event_value
                    if event_id_data == "oTCRn8enMzd":
                        event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                        loop_array['m9'] = event_value
                    if event_id_data == "nTd67mb0PJe":
                        event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                        loop_array['m10'] = event_value
                    if event_id_data == "g3jYfDWMlju":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m11'] = "M-301-1001"
                    if event_id_data == "ezwWMPb12eO":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m12'] = "M-123-1004"
                    if event_id_data == "iifVrszTRRz":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m13'] = "M-123-1018"
                    if event_id_data == "KIZvcIfQvpT":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m14'] = "M-192-1010"
                    if event_id_data == "qs0I9NsfUxu":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m15'] = "M-192-1035"
                    if event_id_data == "YxFGAkRihhj":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m16'] = "M-123-1030"
                    if event_id_data == "x2qkkLksG0N":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m17'] = "M-123-1035"
                    if event_id_data == "uuaO52vR7Sc":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m18'] = "M-192-1016"
                    if event_id_data == "cgKw0UiSSzA":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m19'] = "M-192-1012"
                    if event_id_data == "A0WmBW0xr3Q":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m20'] = "M-121-1020"
                    if event_id_data == "igbaI5cMEch":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m21'] = "M-123-1041"
                    if event_id_data == "tXnR137oYs6":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m22'] = "M-251-4012"
                    if event_id_data == "joyfXYlQ0aS":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m23'] = "M-251-4013"
                    if event_id_data == "Oh5NachZvua":
                        if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                            loop_array['m24'] = "M-181-1018"

                    if event_id_data == "HS5mppnnRUD":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q'] = event_value
                    if event_id_data == "Kzxa8SKjCdp":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q1'] = event_value
                    if event_id_data == "wmkND48fkvf":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q2'] = event_value
                    if event_id_data == "sm78nae74E0":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q3'] = event_value
                    if event_id_data == "YR7bARfLBay":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q4'] = event_value
                    if event_id_data == "Pl3jCeEVYVG":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q5'] = event_value
                    if event_id_data == "J6s8Ju9Y1xk":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q6'] = event_value
                    if event_id_data == "xFAUNJilvDg":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q7'] = event_value
                    if event_id_data == "tn3XjDR6aUt":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q8'] = event_value
                    if event_id_data == "H2g1tcKI0sK":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q9'] = event_value
                    if event_id_data == "wFeFcxSnOO0":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q10'] = event_value
                    if event_id_data == "gTreHa9FsAJ":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q11'] = event_value
                    if event_id_data == "nubIuNPn6kP":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q12'] = event_value
                    if event_id_data == "UOVMe9Hftr8":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q13'] = event_value
                    if event_id_data == "cMVX1z75Uvh":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q14'] = event_value
                    if event_id_data == "B3rbznpTyjJ":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q15'] = event_value
                    if event_id_data == "nxfbinD79RB":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q16'] = event_value    
                    if event_id_data == "BIP1buozD2e":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q17'] = event_value
                    if event_id_data == "xGxzPWNaSuz":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q18'] = event_value
                    if event_id_data == "Fe9k17OVHPe":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q19'] = event_value     
                    if event_id_data == "wiLMg4LNV3V":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q20'] = event_value     
                    if event_id_data == "z8F0ZEgFeeY":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q21'] = event_value     
                    if event_id_data == "btTycEIdfBr":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q22'] = event_value     
                    if event_id_data == "vO16pLLv3u8":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q23'] = event_value     
                    if event_id_data == "mIKc81UxFte":
                        event_value = int(
                            get_event_id_data['dataValues'][numberOfDataValue]['value'])
                        loop_array['q24'] = event_value          
        newest_data.append(loop_array)


# %%
print("--------------------------------Store Data Togather--------------------------------")
if not len(newest_data) == 0:
    jsonStr = json.dumps(newest_data)
    writefile(todayDateTime + "/RowData_" +
              today_date + ".json", json.loads(jsonStr))
    the_big_data_newest_list = []
    for numberOfNewData in range(len(newest_data)):
        newData=newest_data[numberOfNewData]
        sql = "SELECT id FROM RowData WHERE tei = %s AND program = %s AND orgUnit = %s"
        adr = (newData['tei'],newData['program'],newData['orgunit'])
        cursor.execute(sql, adr)
        myresult = cursor.fetchall()
        if(len(myresult)==0):
            sql = "INSERT INTO RowData (tei,program,orgUnit,date,	m,	q,	m1,	q1,	m2,	q2,	m3,	q3,	m4,	q4,	m5,	q5,	m6,	q6,	m7,	q7,	m8,	q8,	m9,	q9,	m10,	q10,	m11,	q11,	m12,	q12,	m13,	q13,	m14,	q14,	m15,	q15,	m16,	q16,	m17,	q17,	m18,	q18,	m19,	q19,	m20,	q20,	m21,	q21,	m22,	q22,	m23,	q23,	m24,	q24,last_update) VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s)"
            val = (newData['tei'],newData['program'],newData['orgunit'],newData['date'],newData['m'], check(newData['q']), newData['m1'], check(newData['q1']), newData['m2'], check(newData['q2']), newData['m3'], check(newData['q3']), newData['m4'], check(newData['q4']) ,newData['m5'], check(newData['q5']), newData['m6'], check(newData['q6']) ,newData['m7'], check(newData['q7']) ,newData['m8'], check(newData['q8']), newData['m9'], check(newData['q9']) ,newData['m10'], check(newData['q10']),newData['m11'], check(newData['q11']), newData['m12'], check(newData['q12']), newData['m13'], check(newData['q13']), newData['m14'], check(newData['q14']), newData['m15'], check(newData['q15']), newData['m16'], check(newData['q16']), newData['m17'], check(newData['q17']), newData['m18'], check(newData['q18']), newData['m19'], check(newData['q19']), newData['m20'], check(newData['q20']), newData['m21'], check(newData['q21']), newData['m22'], check(newData['q22']), newData['m23'], check(newData['q23']), newData['m24'], check(newData['q24']),newData['last_update'])
            cursor.execute(sql, val)
            connection.commit()
            print(cursor.rowcount, "record inserted.")
        else:
            sql = "UPDATE RowData SET m=%s,q=%s,m1=%s,q1=%s,m2=%s,q2=%s,m3=%s,q3=%s,m4=%s,q4=%s,m5=%s,q5=%s,m6=%s,q6=%s,m7=%s,q7=%s,m8=%s,q8=%s,m9=%s,q9=%s,m10=%s,q10=%s,m11=%s,q11=%s,m12=%s,q12=%s,m13=%s,q13=%s,m14=%s,q14=%s,m15=%s,q15=%s,m16=%s,q16=%s,m17=%s,q17=%s,m18=%s,q18=%s,m19=%s,q19=%s,m20=%s,q20=%s,m21=%s,q21=%s,m22=%s,q22=%s,m23=%s,q23=%s,m24=%s,q24=%s , last_update=%s WHERE tei= %s AND program= %s AND orgUnit = %s"
            val = (newData['m'], check(newData['q']), newData['m1'], check(newData['q1']), newData['m2'], check(newData['q2']), newData['m3'], check(newData['q3']), newData['m4'], check(newData['q4']) ,newData['m5'], check(newData['q5']), newData['m6'], check(newData['q6']) ,newData['m7'], check(newData['q7']) ,newData['m8'], check(newData['q8']), newData['m9'], check(newData['q9']) ,newData['m10'], check(newData['q10']),newData['m11'], check(newData['q11']), newData['m12'], check(newData['q12']), newData['m13'], check(newData['q13']), newData['m14'], check(newData['q14']), newData['m15'], check(newData['q15']), newData['m16'], check(newData['q16']), newData['m17'], check(newData['q17']), newData['m18'], check(newData['q18']), newData['m19'], check(newData['q19']), newData['m20'], check(newData['q20']), newData['m21'], check(newData['q21']), newData['m22'], check(newData['q22']), newData['m23'], check(newData['q23']), newData['m24'], check(newData['q24']),newData['last_update'],newData['tei'],newData['program'],newData['orgunit'])
            cursor.execute(sql, val)
            connection.commit()
            print(cursor.rowcount, "record Updated.")
        whereQ='WHERE '
        def InsertNew(mvalue, qvalue,dataElement):
            the_big_data_array = {"tei": newest_data[numberOfNewData]['tei'], "program": newest_data[numberOfNewData]['program'],
                                  "orgunit": newest_data[numberOfNewData]['orgunit'], "date": newest_data[numberOfNewData]['date'],"dataElement":dataElement, "m": mvalue,
                                  "q": qvalue,"edit_date": newest_data[numberOfNewData]['last_update']}
            the_big_data_newest_list.append(the_big_data_array)

        if newest_data[numberOfNewData]['m'] and newest_data[numberOfNewData]['q']:
            InsertNew(newest_data[numberOfNewData]['m'], newest_data[numberOfNewData]['q'],"m")
        if newest_data[numberOfNewData]['m1'] and newest_data[numberOfNewData]['q1']:
            InsertNew(newest_data[numberOfNewData]['m1'], newest_data[numberOfNewData]['q1'],"m1")
        if newest_data[numberOfNewData]['m2'] and newest_data[numberOfNewData]['q2']:
            InsertNew(newest_data[numberOfNewData]['m2'], newest_data[numberOfNewData]['q2'],"m2")
        if newest_data[numberOfNewData]['m3'] and newest_data[numberOfNewData]['q3']:
            InsertNew(newest_data[numberOfNewData]['m3'], newest_data[numberOfNewData]['q3'],"m3")
        if newest_data[numberOfNewData]['m4'] and newest_data[numberOfNewData]['q4']:
            InsertNew(newest_data[numberOfNewData]['m4'], newest_data[numberOfNewData]['q4'],"m4")
        if newest_data[numberOfNewData]['m5'] and newest_data[numberOfNewData]['q5']:
            InsertNew(newest_data[numberOfNewData]['m5'], newest_data[numberOfNewData]['q5'],"m5")
        if newest_data[numberOfNewData]['m6'] and newest_data[numberOfNewData]['q6']:
            InsertNew(newest_data[numberOfNewData]['m6'], newest_data[numberOfNewData]['q6'],"m6")
        if newest_data[numberOfNewData]['m7'] and newest_data[numberOfNewData]['q7']:
            InsertNew(newest_data[numberOfNewData]['m7'], newest_data[numberOfNewData]['q7'],"m7")
        if newest_data[numberOfNewData]['m8'] and newest_data[numberOfNewData]['q8']:
            InsertNew(newest_data[numberOfNewData]['m8'], newest_data[numberOfNewData]['q8'],"m8")
        if newest_data[numberOfNewData]['m9'] and newest_data[numberOfNewData]['q9']:
            InsertNew(newest_data[numberOfNewData]['m9'], newest_data[numberOfNewData]['q9'],"m9")
        if newest_data[numberOfNewData]['m10'] and newest_data[numberOfNewData]['q10']:
            InsertNew(newest_data[numberOfNewData]['m10'], newest_data[numberOfNewData]['q10'],"m10")

        if newest_data[numberOfNewData]['m11'] and newest_data[numberOfNewData]['q11']:
            InsertNew(newest_data[numberOfNewData]['m11'], newest_data[numberOfNewData]['q11'],"m11")
        if newest_data[numberOfNewData]['m12'] and newest_data[numberOfNewData]['q12']:
            InsertNew(newest_data[numberOfNewData]['m12'], newest_data[numberOfNewData]['q12'],"m12")
        if newest_data[numberOfNewData]['m13'] and newest_data[numberOfNewData]['q13']:
            InsertNew(newest_data[numberOfNewData]['m13'], newest_data[numberOfNewData]['q13'],"m13")
        if newest_data[numberOfNewData]['m14'] and newest_data[numberOfNewData]['q14']:
            InsertNew(newest_data[numberOfNewData]['m14'], newest_data[numberOfNewData]['q14'],"m14")
        if newest_data[numberOfNewData]['m15'] and newest_data[numberOfNewData]['q15']:
            InsertNew(newest_data[numberOfNewData]['m15'], newest_data[numberOfNewData]['q15'],"m15")
        if newest_data[numberOfNewData]['m16'] and newest_data[numberOfNewData]['q16']:
            InsertNew(newest_data[numberOfNewData]['m16'], newest_data[numberOfNewData]['q16'],"m16")
        if newest_data[numberOfNewData]['m17'] and newest_data[numberOfNewData]['q17']:
            InsertNew(newest_data[numberOfNewData]['m17'], newest_data[numberOfNewData]['q17'],"m17")
        if newest_data[numberOfNewData]['m18'] and newest_data[numberOfNewData]['q18']:
            InsertNew(newest_data[numberOfNewData]['m18'], newest_data[numberOfNewData]['q18'],"m18")
        if newest_data[numberOfNewData]['m19'] and newest_data[numberOfNewData]['q19']:
            InsertNew(newest_data[numberOfNewData]['m19'], newest_data[numberOfNewData]['q19'],"m19")
        if newest_data[numberOfNewData]['m20'] and newest_data[numberOfNewData]['q20']:
            InsertNew(newest_data[numberOfNewData]['m20'], newest_data[numberOfNewData]['q20'],"m20")
        if newest_data[numberOfNewData]['m21'] and newest_data[numberOfNewData]['q21']:
            InsertNew(newest_data[numberOfNewData]['m21'], newest_data[numberOfNewData]['q21'],"m21")
        if newest_data[numberOfNewData]['m22'] and newest_data[numberOfNewData]['q22']:
            InsertNew(newest_data[numberOfNewData]['m22'], newest_data[numberOfNewData]['q22'],"m22")
        if newest_data[numberOfNewData]['m23'] and newest_data[numberOfNewData]['q23']:
            InsertNew(newest_data[numberOfNewData]['m23'], newest_data[numberOfNewData]['q23'],"m23")
        if newest_data[numberOfNewData]['m24'] and newest_data[numberOfNewData]['q24']:
            InsertNew(newest_data[numberOfNewData]['m24'], newest_data[numberOfNewData]['q24'],"m24")
    jsonStr1 = json.dumps(the_big_data_newest_list)
    for NumberOfMRecord in range(len(the_big_data_newest_list)):
        allMData=the_big_data_newest_list[NumberOfMRecord]
        print(allMData)
        addsql = "SELECT id FROM stock_data WHERE tei = %s AND program = %s AND orgunit = %s AND dataElement = %s"
        addattr = (allMData['tei'],allMData['program'],allMData['orgunit'],allMData['dataElement'])
        cursor.execute(addsql, addattr)
        addresult = cursor.fetchall()
        if(len(addresult)==0):
            insSQL = "INSERT INTO stock_data (tei,program,orgunit,date,dataElement,m,q) VALUES (%s,	%s,	%s,%s,	%s,	%s,%s)"
            insVal = (allMData['tei'],allMData['program'],allMData['orgunit'],allMData['date'],allMData['dataElement'],allMData['m'],allMData['q'])
            cursor.execute(insSQL, insVal)
            connection.commit()
            print(cursor.rowcount, "record inserted.")
        else:
            updateSQL = "UPDATE stock_data SET  m=%s,q=%s,edit_date=%s WHERE tei= %s AND program= %s AND orgunit = %s AND dataElement = %s"
            updateVal = (allMData['m'],allMData['q'],allMData['edit_date'],allMData['tei'],allMData['program'],allMData['orgunit'],allMData['dataElement'])
            cursor.execute(updateSQL, updateVal)
            connection.commit()
            print(cursor.rowcount, "record Updated.")
    # GroupBy Medication Name And OrgUnit With Sum Quantity
    # Store As (GroupData.json)
    print("--------------------------------GroupBy--------------------------------")
    dataFrameFromJson = pd.DataFrame(json.loads(jsonStr1))
    groupby_values = dataFrameFromJson.groupby(['m', 'orgunit'])['q'].sum()
    toJsonFromGroupby = groupby_values.to_json(orient='table')
    writefile(todayDateTime + "/GroupData_" +
              today_date + ".json", json.loads(toJsonFromGroupby))





    # Store all attributeCategoryOptions Data From API
    MappingDataArray = MappingData()
    mapingDataArraytoJson = json.dumps(MappingDataArray)
    fromMappingDataToDataframe = pd.DataFrame(json.loads(mapingDataArraytoJson))
    groupByMappingData = fromMappingDataToDataframe.groupby(fromMappingDataToDataframe['orgunit']).sum()
    newJsonOrgUnit = groupByMappingData.to_json(orient='table')
    newJsonOrgToJson = json.loads(newJsonOrgUnit)
    print(newJsonOrgToJson)
    att_array = []
    attribute_json = []
    for numberOfNewOrgData in range(len(newJsonOrgToJson['data'])):
        org_in_array = newJsonOrgToJson['data'][numberOfNewOrgData]['orgunit']
        print(org_in_array)
        #! A) Get all attribute from dhis2
        att_req = requests.get(
            "https://hmis.moh.ps/tr-dev/api/events?fields=attributeCategoryOptions,event,lastUpdated&orgUnit=" +
            org_in_array+"&program=fnIEoaflGxX",
            auth=HTTPBasicAuth('Saleh', 'Test@123'))
        att_req_data = json.loads(att_req.text)
        print(att_req_data)
        for m in range(len(att_req_data['events'])):
            if att_req_data['events'][m]['attributeCategoryOptions'] not in att_array:
                att_array.append(att_req_data['events']
                                 [m]['attributeCategoryOptions'])
                attribute_json.append({"event": att_req_data['events'][m]['event'], "lastUpdated": att_req_data['events']
                                       [m]['lastUpdated'], "attributeCategoryOptions": att_req_data['events'][m]['attributeCategoryOptions']})
            elif att_req_data['events'][m]['attributeCategoryOptions'] in att_array:
                a_list = [a['lastUpdated'] for a in attribute_json if a['attributeCategoryOptions']
                          == att_req_data['events'][m]['attributeCategoryOptions']]
                var_a = a_list[0]
                var_b = att_req_data['events'][m]['lastUpdated']
                if var_b > var_a:
                    for numberOfNewData in attribute_json:
                        print(attribute_json)
                        if numberOfNewData['attributeCategoryOptions'] == att_req_data['events'][m]['attributeCategoryOptions']:
                            numberOfNewData['event'] = att_req_data['events'][m]['event']
                            numberOfNewData['lastUpdated'] = att_req_data['events'][m]['lastUpdated']
                        for fgtr in range(len(att_array)):
                            print(att_array[fgtr])  
                            if(att_array[fgtr] == numberOfNewData['attributeCategoryOptions']):
                                att_array[fgtr] = att_req_data['events'][m]['attributeCategoryOptions']
                                print(att_array[fgtr])











    # Multiple Loop to check if event exist or not
    Update_response_array = []
    Create_response_array = []
    print(MappingDataArray)
    print(att_array)
    print("--------------------------------Update Data Stage--------------------------------")
    for p in range(len(MappingDataArray)):
        mappingArrayCode = MappingDataArray[p]['mCode']
        mappingArrayorgunit = MappingDataArray[p]['orgunit']
        print(mappingArrayCode)
        print(mappingArrayorgunit)
        if(mappingArrayCode not in att_array):
            data = {
                "status": "COMPLETED",
                "program": "fnIEoaflGxX",
                "programStage": "fdRCUlObMnG",
                "enrollment": "lzL2rq6vcqw",
                "enrollmentStatus": "ACTIVE",
                "orgUnit": MappingDataArray[p]['orgunit'],
                "eventDate": today_date,
                "dataValues": [
                    {
                        "value": MappingDataArray[p]['quantity'],
                        "dataElement": "LijzB622Z22"
                    }
                ],
                "attributeOptionCombo": "bTHXxcpisuk",
                "attributeCategoryOptions": mappingArrayCode
            }
            print(data)
            headers = {'Content-Type': 'application/json'}
            #! B) Insert New Event to dhis2
            create_event = requests.post("https://hmis.moh.ps/tr-dev/api/events",
                                         data=json.dumps(data), headers=headers, auth=HTTPBasicAuth('Saleh', 'Test@123'))
            att_req_data = json.loads(create_event.text)
            Create_response_array.append(att_req_data)
            print("Create Stock Successfully")
        elif(mappingArrayCode in att_array):
            for t in range(len(attribute_json)):
                print("attributeCategoryOptions")
                print(attribute_json[t]['attributeCategoryOptions'])
                print("mappingArrayCode")
                print(mappingArrayCode)
                if(attribute_json[t]['attributeCategoryOptions'] == mappingArrayCode):
                    storeEventId = attribute_json[t]['event']
            #! C) Get every event quantity value
                    event_req = requests.get(
                        "https://hmis.moh.ps/tr-dev/api/events/"+storeEventId, auth=HTTPBasicAuth('Saleh', 'Test@123'))
                    selected_event_data = json.loads(event_req.text)
                    x_number_on = 0
                    for r in range(len(selected_event_data['dataValues'])):
                        if(selected_event_data['dataValues'][r]['dataElement'] == 'LijzB622Z22'):
                            x_number_on = 1
                            old_q_value = int(
                                selected_event_data['dataValues'][r]['value'])
                            new_q_value = int(
                                MappingDataArray[p]['quantity'])
                            sum_value = old_q_value+new_q_value
                            selected_event_data['dataValues'][r]['value'] = sum_value
                            data = json.dumps(selected_event_data)
                            headers = {'Content-Type': 'application/json'}
                #! D) Insert New quantity to dhis2
                            Update_req = requests.put(
                                "https://hmis.moh.ps/tr-dev/api/events/"+storeEventId, data=data, headers=headers, auth=HTTPBasicAuth('Saleh', 'Test@123'))
                            Update_response = json.loads(Update_req.text)
                            Update_response_array.append(Update_response)
                            print("Update Stock Successfully")
                    if(x_number_on != 1):
                        just_new = {"value": int(
                            MappingDataArray[p]['quantity']), "dataElement": "LijzB622Z22"}
                        selected_event_data['dataValues'].append(just_new)
                        data = json.dumps(selected_event_data)
                #! Update Stock Successfully And Create New DataElement
                        Update_req = requests.put(
                            "https://hmis.moh.ps/tr-dev/api/events/"+storeEventId, data=data, headers=headers, auth=HTTPBasicAuth('Saleh', 'Test@123'))
                        Update_response = json.loads(Update_req.text)
                        Update_response_array.append(Update_response)
                        print("Update Stock Successfully And Create New DataElement")
    writefile(todayDateTime+"/Update_ImportSummaries_" +
              today_date+".json", Update_response_array)
    writefile(todayDateTime+"/Create_ImportSummaries_" +
              today_date+".json", Create_response_array)
    print(datetime.now()-Start_DateTime)
else:
    print("EmptyData")
    writefile(todayDateTime + "/JobSummary" +
              today_date + ".json", json.dumps([{"0": "EmptyData"}]))
