# %% [markdown]
# # import all librarys

# %%
# !pip3 install pandas
# !pip3 install requests
# !pip3 install os
# !pip3 install HTTPBasicAuth

# %%
# # !pip3 uninstall mysqlclient
# # !pip3 uninstall mysql-connector-python
# # !pip3 uninstall mysql
# !pip3 install mysql-connector-python

# %%
import json
import pandas as pd
import requests
import os
import mysql.connector
from mysql.connector import Error
from requests.auth import HTTPBasicAuth
from datetime import date
from datetime import datetime
import time

# %% [markdown]
# # Connect With Database

# %%
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='stock',
                                         user='root',
                                         port=8889,
                                         password='root', ssl_disabled=True)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
except Error as e:
    print("Error while connecting to MySQL", e)

# %% [markdown]
# # General Definition

# %%
#define all variables
categoryOptionsList = []
today = date.today()
newest_data = []
Create_response_array=[]
Start_DateTime = datetime.now()
print("Start At: ", Start_DateTime)
today_date = today.strftime("%Y-%m-%d")
todayDateTime = "LOG/Stock_" + str(datetime.now())
path = '/Users/salehabbas/Developer/Python/pharmacy_stock/' + todayDateTime
#Create Folder if not exsist
try:
    os.mkdir(path)
except OSError as error:
    print(error)

# %% [markdown]
# # All Founctions

# %%
def writefile(FileName, Data):
    json_data = json.dumps(Data, ensure_ascii=False)
    file = open(FileName, "w")
    with open(file.name, "w") as files:
        files.write(json_data)
    file.close()
def category_options():
    category_options_req = requests.get(
        "https://hmis.moh.ps/tr-dev-integration/api/categoryOptions?fields=id,code",
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
def GetCodeData(mName):
    with open('categoryOptions.json') as categoryOptionsFile:
         catFile = json.load(categoryOptionsFile)
         MappingList=list(filter(lambda x:x["code"]==mName,catFile))
         return MappingList[0]['id']
def InsertNew(mvalue, qvalue,dataElement):
    the_big_data_array = {"tei": newest_data[numberOfNewData]['tei'], "program": newest_data[numberOfNewData]['program'],
                            "orgunit": newest_data[numberOfNewData]['orgunit'], "date": newest_data[numberOfNewData]['date'],"dataElement":dataElement, "m": mvalue,
                            "q": qvalue,"edit_date": newest_data[numberOfNewData]['last_update']}
    the_big_data_newest_list.append(the_big_data_array)
def createEventFunction(orgUnitId,xEqValue,midicaneId):
        data = {
                        "status": "ACTIVE",
                        "program": "fnIEoaflGxX",
                        "enrollment": "lzL2rq6vcqw",
                        "enrollmentStatus": "ACTIVE",
                        "orgUnit": orgUnitId,
                        "eventDate": today_date,
                        "dataValues": [
                            {
                                "value": xEqValue,
                                "dataElement": "LijzB622Z22"
                            },
                             {
                                "dataElement": "bry41dJZ99x",
                                "value": -xEqValue,
                            },
                        ],
                        "attributeCategoryOptions": midicaneId
                    }
        print(data)
        headers = {'Content-Type': 'application/json'}
            #! B) Insert New Event to dhis2
        # if midicaneId=="OoW5rFRsxF3":
        create_event = requests.post("https://hmis.moh.ps/tr-dev-integration/api/events",
                                        data=json.dumps(data), headers=headers, auth=HTTPBasicAuth('Saleh', 'Test@123'))
        # print(create_event.request.body)
        att_req_data = json.loads(create_event.text)
        Create_response_array.append(att_req_data)
        print("Create Stock Successfully")
        print(att_req_data)
def updateEventFunction(eventId,eventData):
    headers = {'Content-Type': 'application/json'}
    try:
        update_event = requests.put('https://hmis.moh.ps/tr-dev-integration/api/events/'+eventId, data =eventData,headers=headers, auth=HTTPBasicAuth('Saleh', 'Test@123'))
        att_req_data = json.loads(update_event.text)
        print(att_req_data)
        print("Update Event Stock Successfully")
    except:
        print("An exception occurred")
def get_all_time_entries():
    url_address = "https://hmis.moh.ps/tr-dev-integration/api/events?program=fnIEoaflGxX"  
    headers = {'Content-Type': 'application/json'}

    # find out total number of pages
    r = requests.get(url=url_address, headers=headers, auth=HTTPBasicAuth('Saleh', 'Test@123')).json()
    total_pages = int(r['pager']['pageCount'])

    # results will be appended to this list
    all_time_entries = []

    # loop through all pages and return JSON object
    for page in range(0, total_pages):

        url = "https://hmis.moh.ps/tr-dev-integration/api/events?page="+str(page)+"&program=fnIEoaflGxX"              
        response = requests.get(url=url, headers=headers, auth=HTTPBasicAuth('Saleh', 'Test@123')).json()        
        all_time_entries.append(response)       
        page += 1

    # prettify JSON
    data = json.dumps(all_time_entries, sort_keys=True, indent=4)
    writefile('events.json',json.loads(data))
    print('Update Event File')

# %% [markdown]
# # Mapping Medicane with Code

# %%
print("--------------------------------Mapping And Store attributeCategoryOptions--------------------------------")
if not os.path.exists('categoryOptions.json'):
    category_options()

# %% [markdown]
# # Start Loop
# -> Get all org
# --> Get all tei for all org
# ---> Get all event for every tei
# ----> Get all data for every event
# > Output [newest_data]

# %%
print("--------------------------------Start Loop------------------------")
    #! 1) Get All Org Unit
get_org_unit_req = requests.get(
    "https://hmis.moh.ps/tr-dev-integration/api/programs/fnIEoaflGxX?fields=organisationUnits",
    auth=HTTPBasicAuth('Saleh', 'Test@123'))
# print(get_org_unit_req.url)
get_org_unit_data = json.loads(get_org_unit_req.text)
for dataFromOrgUnit in range(len(get_org_unit_data['organisationUnits'])):
    org_unit_id = get_org_unit_data['organisationUnits'][dataFromOrgUnit]['id']
    # ! 2) Get all TEI For This orgUnit
    get_tei = requests.get(
        "https://hmis.moh.ps/tr-dev-integration/api/trackedEntityInstances?ou=" +
        org_unit_id+"&fields=trackedEntityInstance&lastUpdatedEndDate="
        + today_date + "&lastUpdatedStartDate=" + today_date,
        auth=HTTPBasicAuth('Saleh', 'Test@123'))
    # print(get_tei.url)
    get_tei_data = json.loads(get_tei.text)
    if('trackedEntityInstances' in get_tei_data):
        for numberOfTEI in range(len(get_tei_data['trackedEntityInstances'])):
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
                "https://hmis.moh.ps/tr-dev-integration/api/events?trackedEntityInstance=" + tei_id + "&lastUpdatedEndDate=" +
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
                    "https://hmis.moh.ps/tr-dev-integration/api/events/" + event_id, auth=HTTPBasicAuth('Saleh', 'Test@123'))
                get_event_id_data = json.loads(get_event_id.text)
                loop_array['date'] = str(datetime.strptime(get_event_id_data['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date())
                loop_array['last_update'] = str(datetime.strptime(get_event_id_data['dueDate'], '%Y-%m-%dT%H:%M:%S.%f').date())
                #? Store all variables into array
                if('dataValues' in json.dumps(get_event_id_data)):
                    for numberOfDataValue in range(len(get_event_id_data['dataValues'])):
                        event_id_data = get_event_id_data['dataValues'][numberOfDataValue]['dataElement']
                        if event_id_data == "aM2Vn0UUPJB":
                            event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                            loop_array['m'] = GetCodeData(event_value)
                        if event_id_data == "WSeukMBwbQ3":
                            event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                            loop_array['m1'] = GetCodeData(event_value)
                        if event_id_data == "TORfS27wR0q":
                            event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                            loop_array['m2'] = GetCodeData(event_value)
                        if event_id_data == "TnrWDEL4PoR":
                            event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                            loop_array['m3'] = GetCodeData(event_value)
                        if event_id_data == "iy166uomfXk":
                            event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                            loop_array['m4'] = GetCodeData(event_value)
                        if event_id_data == "ntECq4xEo24":
                            event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                            loop_array['m5'] = GetCodeData(event_value)
                        if event_id_data == "Ne2veOUhPw0":
                            event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                            loop_array['m6'] = GetCodeData(event_value)
                        if event_id_data == "R2rxr1Z8i4v":
                            event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                            loop_array['m7'] = GetCodeData(event_value)
                        if event_id_data == "Dlx79ePwf1g":
                            event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                            loop_array['m8'] = GetCodeData(event_value)
                        if event_id_data == "oTCRn8enMzd":
                            event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                            loop_array['m9'] = GetCodeData(event_value)
                        if event_id_data == "nTd67mb0PJe":
                            event_value = get_event_id_data['dataValues'][numberOfDataValue]['value']
                            loop_array['m10'] = GetCodeData(event_value)
                        if event_id_data == "g3jYfDWMlju":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m11'] = GetCodeData("M-301-1001")
                        if event_id_data == "ezwWMPb12eO":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m12'] = GetCodeData("M-123-1004")
                        if event_id_data == "iifVrszTRRz":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m13'] =  GetCodeData("M-123-1018")
                        if event_id_data == "KIZvcIfQvpT":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m14'] = GetCodeData("M-192-1010")
                        if event_id_data == "qs0I9NsfUxu":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m15'] = GetCodeData("M-192-1035")
                        if event_id_data == "YxFGAkRihhj":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m16'] =  GetCodeData("M-123-1030")
                        if event_id_data == "x2qkkLksG0N":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m17'] = GetCodeData("M-123-1035")
                        if event_id_data == "uuaO52vR7Sc":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m18'] = GetCodeData("M-192-1016")
                        if event_id_data == "cgKw0UiSSzA":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m19'] =  GetCodeData("M-192-1012")
                        if event_id_data == "A0WmBW0xr3Q":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m20'] =  GetCodeData("M-121-1020")
                        if event_id_data == "igbaI5cMEch":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m21'] = GetCodeData("M-123-1041")
                        if event_id_data == "tXnR137oYs6":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m22'] =  GetCodeData("M-251-4012")
                        if event_id_data == "joyfXYlQ0aS":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m23'] =  GetCodeData("M-251-4013")
                        if event_id_data == "Oh5NachZvua":
                            if get_event_id_data['dataValues'][numberOfDataValue]['value']:
                                loop_array['m24'] =  GetCodeData("M-181-1018")

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

# %% [markdown]
# # Update Database if we have new Data

# %%
print("--------------------------------Store Data Togather--------------------------------")
#if array not empty
if not len(newest_data) == 0:
    jsonStr = json.dumps(newest_data)
    #write array data to RowData File
    writefile(todayDateTime + "/RowData_" +
              today_date + ".json", json.loads(jsonStr))
    the_big_data_newest_list = []
    for numberOfNewData in range(len(newest_data)):
        newData=newest_data[numberOfNewData]
        #check if this row of data exsist or not
        sql = "SELECT id FROM RowData WHERE tei = %s AND program = %s AND orgUnit = %s"
        adr = (newData['tei'],newData['program'],newData['orgunit'])
        cursor.execute(sql, adr)
        myresult = cursor.fetchall()
        if(len(myresult)==0):
            #if not exsist insert new row to database
            sql = "INSERT INTO RowData (tei,program,orgUnit,date,	m,	q,	m1,	q1,	m2,	q2,	m3,	q3,	m4,	q4,	m5,	q5,	m6,	q6,	m7,	q7,	m8,	q8,	m9,	q9,	m10,	q10,	m11,	q11,	m12,	q12,	m13,	q13,	m14,	q14,	m15,	q15,	m16,	q16,	m17,	q17,	m18,	q18,	m19,	q19,	m20,	q20,	m21,	q21,	m22,	q22,	m23,	q23,	m24,	q24,last_update) VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s)"
            val = (newData['tei'],newData['program'],newData['orgunit'],newData['date'],newData['m'], check(newData['q']), newData['m1'], check(newData['q1']), newData['m2'], check(newData['q2']), newData['m3'], check(newData['q3']), newData['m4'], check(newData['q4']) ,newData['m5'], check(newData['q5']), newData['m6'], check(newData['q6']) ,newData['m7'], check(newData['q7']) ,newData['m8'], check(newData['q8']), newData['m9'], check(newData['q9']) ,newData['m10'], check(newData['q10']),newData['m11'], check(newData['q11']), newData['m12'], check(newData['q12']), newData['m13'], check(newData['q13']), newData['m14'], check(newData['q14']), newData['m15'], check(newData['q15']), newData['m16'], check(newData['q16']), newData['m17'], check(newData['q17']), newData['m18'], check(newData['q18']), newData['m19'], check(newData['q19']), newData['m20'], check(newData['q20']), newData['m21'], check(newData['q21']), newData['m22'], check(newData['q22']), newData['m23'], check(newData['q23']), newData['m24'], check(newData['q24']),newData['last_update'])
            cursor.execute(sql, val)
            connection.commit()
            print(cursor.rowcount, "record inserted.")
        else:
            #if exsist update the row
            sql = "UPDATE RowData SET m=%s,q=%s,m1=%s,q1=%s,m2=%s,q2=%s,m3=%s,q3=%s,m4=%s,q4=%s,m5=%s,q5=%s,m6=%s,q6=%s,m7=%s,q7=%s,m8=%s,q8=%s,m9=%s,q9=%s,m10=%s,q10=%s,m11=%s,q11=%s,m12=%s,q12=%s,m13=%s,q13=%s,m14=%s,q14=%s,m15=%s,q15=%s,m16=%s,q16=%s,m17=%s,q17=%s,m18=%s,q18=%s,m19=%s,q19=%s,m20=%s,q20=%s,m21=%s,q21=%s,m22=%s,q22=%s,m23=%s,q23=%s,m24=%s,q24=%s , last_update=%s WHERE tei= %s AND program= %s AND orgUnit = %s"
            val = (newData['m'], check(newData['q']), newData['m1'], check(newData['q1']), newData['m2'], check(newData['q2']), newData['m3'], check(newData['q3']), newData['m4'], check(newData['q4']) ,newData['m5'], check(newData['q5']), newData['m6'], check(newData['q6']) ,newData['m7'], check(newData['q7']) ,newData['m8'], check(newData['q8']), newData['m9'], check(newData['q9']) ,newData['m10'], check(newData['q10']),newData['m11'], check(newData['q11']), newData['m12'], check(newData['q12']), newData['m13'], check(newData['q13']), newData['m14'], check(newData['q14']), newData['m15'], check(newData['q15']), newData['m16'], check(newData['q16']), newData['m17'], check(newData['q17']), newData['m18'], check(newData['q18']), newData['m19'], check(newData['q19']), newData['m20'], check(newData['q20']), newData['m21'], check(newData['q21']), newData['m22'], check(newData['q22']), newData['m23'], check(newData['q23']), newData['m24'], check(newData['q24']),newData['last_update'],newData['tei'],newData['program'],newData['orgunit'])
            cursor.execute(sql, val)
            connection.commit()
            print(cursor.rowcount, "record Updated.")
        whereQ='WHERE '+"tei= '"+ newest_data[numberOfNewData]['tei']+"' AND program = '"+ newest_data[numberOfNewData]['program']+"' AND orgunit='"+ newest_data[numberOfNewData]['orgunit']+"'"
        if newest_data[numberOfNewData]['m'] and newest_data[numberOfNewData]['q']:
            InsertNew(newest_data[numberOfNewData]['m'], newest_data[numberOfNewData]['q'],"m")
            whereQ=whereQ+" AND dataElement != 'm'"
        if newest_data[numberOfNewData]['m1'] and newest_data[numberOfNewData]['q1']:
            InsertNew(newest_data[numberOfNewData]['m1'], newest_data[numberOfNewData]['q1'],"m1")
            whereQ=whereQ+" AND dataElement != 'm1'"
        if newest_data[numberOfNewData]['m2'] and newest_data[numberOfNewData]['q2']:
            InsertNew(newest_data[numberOfNewData]['m2'], newest_data[numberOfNewData]['q2'],"m2")
            whereQ=whereQ+" AND dataElement != 'm2'"
        if newest_data[numberOfNewData]['m3'] and newest_data[numberOfNewData]['q3']:
            InsertNew(newest_data[numberOfNewData]['m3'], newest_data[numberOfNewData]['q3'],"m3")
            whereQ=whereQ+" AND dataElement != 'm3'"
        if newest_data[numberOfNewData]['m4'] and newest_data[numberOfNewData]['q4']:
            InsertNew(newest_data[numberOfNewData]['m4'], newest_data[numberOfNewData]['q4'],"m4")
            whereQ=whereQ+" AND dataElement != 'm4'"
        if newest_data[numberOfNewData]['m5'] and newest_data[numberOfNewData]['q5']:
            InsertNew(newest_data[numberOfNewData]['m5'], newest_data[numberOfNewData]['q5'],"m5")
            whereQ=whereQ+" AND dataElement != 'm5'"
        if newest_data[numberOfNewData]['m6'] and newest_data[numberOfNewData]['q6']:
            InsertNew(newest_data[numberOfNewData]['m6'], newest_data[numberOfNewData]['q6'],"m6")
            whereQ=whereQ+" AND dataElement != 'm6'"
        if newest_data[numberOfNewData]['m7'] and newest_data[numberOfNewData]['q7']:
            InsertNew(newest_data[numberOfNewData]['m7'], newest_data[numberOfNewData]['q7'],"m7")
            whereQ=whereQ+" AND dataElement != 'm7'"
        if newest_data[numberOfNewData]['m8'] and newest_data[numberOfNewData]['q8']:
            InsertNew(newest_data[numberOfNewData]['m8'], newest_data[numberOfNewData]['q8'],"m8")
            whereQ=whereQ+" AND dataElement != 'm8'"
        if newest_data[numberOfNewData]['m9'] and newest_data[numberOfNewData]['q9']:
            InsertNew(newest_data[numberOfNewData]['m9'], newest_data[numberOfNewData]['q9'],"m9")
            whereQ=whereQ+" AND dataElement != 'm9'"
        if newest_data[numberOfNewData]['m10'] and newest_data[numberOfNewData]['q10']:
            InsertNew(newest_data[numberOfNewData]['m10'], newest_data[numberOfNewData]['q10'],"m10")
            whereQ=whereQ+" AND dataElement != 'm10'"
        if newest_data[numberOfNewData]['m11'] and newest_data[numberOfNewData]['q11']:
            InsertNew(newest_data[numberOfNewData]['m11'], newest_data[numberOfNewData]['q11'],"m11")
            whereQ=whereQ+" AND dataElement != 'm11'"
        if newest_data[numberOfNewData]['m12'] and newest_data[numberOfNewData]['q12']:
            InsertNew(newest_data[numberOfNewData]['m12'], newest_data[numberOfNewData]['q12'],"m12")
            whereQ=whereQ+" AND dataElement != 'm12'"
        if newest_data[numberOfNewData]['m13'] and newest_data[numberOfNewData]['q13']:
            InsertNew(newest_data[numberOfNewData]['m13'], newest_data[numberOfNewData]['q13'],"m13")
            whereQ=whereQ+" AND dataElement != 'm13'"
        if newest_data[numberOfNewData]['m14'] and newest_data[numberOfNewData]['q14']:
            InsertNew(newest_data[numberOfNewData]['m14'], newest_data[numberOfNewData]['q14'],"m14")
            whereQ=whereQ+" AND dataElement != 'm14'"
        if newest_data[numberOfNewData]['m15'] and newest_data[numberOfNewData]['q15']:
            InsertNew(newest_data[numberOfNewData]['m15'], newest_data[numberOfNewData]['q15'],"m15")
            whereQ=whereQ+" AND dataElement != 'm15'"
        if newest_data[numberOfNewData]['m16'] and newest_data[numberOfNewData]['q16']:
            InsertNew(newest_data[numberOfNewData]['m16'], newest_data[numberOfNewData]['q16'],"m16")
            whereQ=whereQ+" AND dataElement != 'm16'"
        if newest_data[numberOfNewData]['m17'] and newest_data[numberOfNewData]['q17']:
            InsertNew(newest_data[numberOfNewData]['m17'], newest_data[numberOfNewData]['q17'],"m17")
            whereQ=whereQ+" AND dataElement != 'm17'"
        if newest_data[numberOfNewData]['m18'] and newest_data[numberOfNewData]['q18']:
            InsertNew(newest_data[numberOfNewData]['m18'], newest_data[numberOfNewData]['q18'],"m18")
            whereQ=whereQ+" AND dataElement != 'm18'"
        if newest_data[numberOfNewData]['m19'] and newest_data[numberOfNewData]['q19']:
            InsertNew(newest_data[numberOfNewData]['m19'], newest_data[numberOfNewData]['q19'],"m19")
            whereQ=whereQ+" AND dataElement != 'm19'"
        if newest_data[numberOfNewData]['m20'] and newest_data[numberOfNewData]['q20']:
            InsertNew(newest_data[numberOfNewData]['m20'], newest_data[numberOfNewData]['q20'],"m20")
            whereQ=whereQ+" AND dataElement != 'm20'"
        if newest_data[numberOfNewData]['m21'] and newest_data[numberOfNewData]['q21']:
            InsertNew(newest_data[numberOfNewData]['m21'], newest_data[numberOfNewData]['q21'],"m21")
            whereQ=whereQ+" AND dataElement != 'm21'"
        if newest_data[numberOfNewData]['m22'] and newest_data[numberOfNewData]['q22']:
            InsertNew(newest_data[numberOfNewData]['m22'], newest_data[numberOfNewData]['q22'],"m22")
            whereQ=whereQ+" AND dataElement != 'm22'"
        if newest_data[numberOfNewData]['m23'] and newest_data[numberOfNewData]['q23']:
            InsertNew(newest_data[numberOfNewData]['m23'], newest_data[numberOfNewData]['q23'],"m23")
            whereQ=whereQ+" AND dataElement != 'm23'"
        if newest_data[numberOfNewData]['m24'] and newest_data[numberOfNewData]['q24']:
            InsertNew(newest_data[numberOfNewData]['m24'], newest_data[numberOfNewData]['q24'],"m24")
            whereQ=whereQ+" AND dataElement != 'm24'"
        #delete from stock data where record not equal data
        deleteQ = "DELETE FROM stock_data "+whereQ
        print(deleteQ)
        cursor.execute(deleteQ)
        deleteresult = cursor.fetchall()
        print(len(deleteresult))
    
    #GET all medicane with quantity and check on stock data (database)
    jsonStr1 = json.dumps(the_big_data_newest_list)
    for NumberOfMRecord in range(len(the_big_data_newest_list)):
        allMData=the_big_data_newest_list[NumberOfMRecord]
        addsql = "SELECT id FROM stock_data WHERE tei = %s AND program = %s AND orgUnit = %s AND dataElement = %s"
        addattr = (allMData['tei'],allMData['program'],allMData['orgunit'],allMData['dataElement'])
        cursor.execute(addsql, addattr)
        addresult = cursor.fetchall()
        if(len(addresult)==0):
            #if not exsist then insert new record 
            insSQL = "INSERT INTO stock_data (tei, program, orgunit, date, dataElement, m, q) VALUES (%s ,%s , %s,%s,	%s,	%s,%s)"
            insVal = (allMData['tei'], allMData['program'], allMData['orgunit'], allMData['date'], allMData['dataElement'], allMData['m'], allMData['q'])
            cursor.execute(insSQL, insVal)
            connection.commit()
            print(cursor.rowcount, "record inserted.")
        else:
            #if exsist then update record 
            updateSQL = "UPDATE stock_data SET  m=%s, q=%s, edit_date=%s WHERE tei= %s AND program= %s AND orgUnit = %s AND dataElement = %s"
            updateVal = (allMData['m'],allMData['q'],allMData['edit_date'],allMData['tei'],allMData['program'],allMData['orgunit'],allMData['dataElement'])
            cursor.execute(updateSQL, updateVal)
            connection.commit()
            print(cursor.rowcount, "record Updated.")
    #select and store all stock data by medicane and orgunit
    sumQ = "SELECT orgunit,m,SUM(q) AS q FROM stock_data GROUP BY m,orgunit"
    cursor.execute(sumQ)
    sumResult = cursor.fetchall()
    mydict = []
    print(sumResult)
    for row in sumResult:
        mydict.append({"orgunit":row[0],"m":row[1],"q":str(row[2])})
    stud_json = json.dumps(mydict)
    print(stud_json)
else:
    print("EmptyData")
    writefile(todayDateTime + "/JobSummary" +
              today_date + ".json", json.dumps([{"0": "EmptyData"}]))

# %% [markdown]
# # Store All Event for this program

# %%
#get all dhis2 event and store on json
get_all_time_entries()

# %% [markdown]
# # Start Loop on all Medicane

# %%
#Load last updated list from database
databaseList=json.loads(stud_json)
for sumList in range(len(databaseList)):
    #define Arrays
    activeEventArray=[]
    notActiveEventArray=[]
    forNegArray=[]
    #define variables from database data
    orgUnitId=databaseList[sumList]['orgunit']#! Org
    midicaneId=databaseList[sumList]['m']#! M
    quantityDispensed=databaseList[sumList]['q'] #! Q
    print("midicaneId:",midicaneId)
    print("quantityDispensed:",quantityDispensed)
    completed=0
    active=0
    with open('events.json') as event:
        eventFile = json.load(event)
        # print(json.dumps(eventFile[0]['events']))
        for numberOfEvent in range(len(eventFile[0]['events'])):
            eventArray=eventFile[0]['events'][numberOfEvent]
            if(eventArray['attributeCategoryOptions']==midicaneId):
                if(eventArray['status']=='ACTIVE'):
                    for numberOfDataValue in range(len(eventArray['dataValues'])):
                        if(eventArray['dataValues'][numberOfDataValue]['dataElement']=='LijzB622Z22'):
                            active= active+int(eventArray['dataValues'][numberOfDataValue]['value'])
                elif(eventArray['status']=='COMPLETED'):
                     for numberOfDataValue in range(len(eventArray['dataValues'])):
                            if(eventArray['dataValues'][numberOfDataValue]['dataElement']=='LijzB622Z22'):
                                 completed= completed+int(eventArray['dataValues'][numberOfDataValue]['value'])
        print("completed:", completed)
        print("active:", active)
        xEqValue=int(quantityDispensed)-(completed+active)
        print("total:", xEqValue)

        if(xEqValue>0 or xEqValue<0):
            for numberOfEvent in range(len(eventFile[0]['events'])):
                eventArray=eventFile[0]['events'][numberOfEvent]
                if(eventArray['attributeCategoryOptions']==midicaneId):
                    active=False
                    notExpired=False
                    totalDisposed=0
                    eventValue=False
                    totalValue=None
                    eventTotalValue=None
                    if(eventArray['status']=='ACTIVE'):
                        active=True
                    for numberOfDataValue in range(len(eventArray['dataValues'])):
                        if(eventArray['dataValues'][numberOfDataValue]['dataElement']=='xW95VLnIqyP'):
                            valueDate = datetime. strptime(eventArray['dataValues'][numberOfDataValue]['value'], '%Y-%m-%d').date()
                            todayDateValue =  datetime. strptime(today.strftime( '%Y-%m-%d'), '%Y-%m-%d').date()
                            if(todayDateValue<=valueDate):
                                notExpired=True
                            else:
                                notExpired=False
                        else:
                            notExpired=True
                        if(eventArray['dataValues'][numberOfDataValue]['dataElement']=='LijzB622Z22'):
                            eventValue=int(eventArray['dataValues'][numberOfDataValue]['value'])
                        if(eventArray['dataValues'][numberOfDataValue]['dataElement']=='bry41dJZ99x'):
                            totalValue=int(eventArray['dataValues'][numberOfDataValue]['value'])
                        if(eventArray['dataValues'][numberOfDataValue]['dataElement']=='eskqGfai0gc'):
                             eventTotalValue=int(eventArray['dataValues'][numberOfDataValue]['value'])
                    if(active and notExpired):
                        print("in")
                        # print({"event":eventArray['event'],"date":datetime. strptime(eventArray['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"value":eventValue,"total":totalValue,"query":eventArray})
                        activeEventArray.append({"event":eventArray['event'],"date":datetime. strptime(eventArray['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"value":eventValue,"total":totalValue,"query":eventArray})
                        forNegArray.append({"event":eventArray['event'],"date":datetime. strptime(eventArray['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"stock":eventTotalValue,"value":eventValue,"total":totalValue,"query":eventArray})
                    else:
                        print("out")
                        datexxx=datetime. strptime(eventArray['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date() if eventArray['eventDate']!=None else ''
                        # print({"event":eventArray['event'],"date":datexxx,"value":eventValue,"total":totalValue,"query":eventArray})
                        notActiveEventArray.append({"event":datexxx ,"date":datetime. strptime(eventArray['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"stock":eventTotalValue,"value":eventValue,"total":totalValue,"query":eventArray})
                        forNegArray.append({"event":eventArray['event'],"date":datetime. strptime(eventArray['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"stock":eventTotalValue,"value":eventValue,"total":totalValue,"query":eventArray})
        else:
            print("Equal Zero")
        
        if(xEqValue==0):
            print("No Edit")
        
        elif( xEqValue>0):
            print("Edit Positive")
            #! Create New Event
            if(len(activeEventArray)==0):
                print('=0')
                createEventFunction(orgUnitId,xEqValue,midicaneId)
            #! Update Exsisted Event
            elif(len(activeEventArray)>0):
                print('>')
                sorted_date_array = sorted(activeEventArray, key=lambda x: x['date'])
                swapArray=sorted_date_array[0]['total']
                eventSelectID=''
                for EventJsonArray in range(len(sorted_date_array)):
                    if  sorted_date_array[EventJsonArray]['total'] >= swapArray:
                        swapArray= sorted_date_array[EventJsonArray]['total']
                        eventSelectID=sorted_date_array[EventJsonArray]['event']
                print(eventSelectID)
                selectedData=list(filter(lambda x:x["event"]==eventSelectID,sorted_date_array))
                print(selectedData)
                if selectedData[0]['total']>0:
                    #! add to oldes one
                    print('-----')
                    print(sorted_date_array[0])
                    newEventValue=sorted_date_array[0]['total']-xEqValue
                    valueAdded=sorted_date_array[0]['value']+xEqValue
                    print(newEventValue)
                    print(valueAdded)
                    updateEventId=sorted_date_array[0]['event']
                    for numberOfDataElement in range(len(sorted_date_array[0]['query']['dataValues'])):
                        if(sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['dataElement']=='LijzB622Z22'):
                            sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['value']=valueAdded
                        if(sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['dataElement']=='bry41dJZ99x'):
                                sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['value']=newEventValue
                    toJsonFromEventData=json.dumps(sorted_date_array[0]['query'])
                    eventWithNewData=json.loads(toJsonFromEventData)
                    updateEventFunction(updateEventId,toJsonFromEventData)
                else: 
                    newEventValue=xEqValue-sorted_date_array[EventJsonArray]['total']
                    valueAdded=xEqValue-newEventValue
                    updatedValueWithAdded=valueAdded+sorted_date_array[EventJsonArray]['value']
                    updateEventId=sorted_date_array[EventJsonArray]['event']
                    for numberOfDataElement in range(len(sorted_date_array[EventJsonArray]['query']['dataValues'])):
                        if(sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['dataElement']=='LijzB622Z22'):
                            sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['value']= updatedValueWithAdded
                    sorted_date_array[EventJsonArray]['query']['status']='COMPLETED'
                    toJsonFromEventData=json.dumps(sorted_date_array[EventJsonArray]['query'])
                    eventWithNewData=json.loads(toJsonFromEventData)
                    updateEventFunction(updateEventId,toJsonFromEventData)
                    if(newEventValue==0):
                        print('break')
                        break
                    else:
                        if(len(activeEventArray)>0):
                            xEqValue=newEventValue
                            activeEventArray.pop(0)
                            if(len(activeEventArray)==0 and xEqValue !=0):
                                createEventFunction(orgUnitId,xEqValue,midicaneId)
                                xEqValue=0

        elif(xEqValue<0):
            # print(forNegArray)
            print("Edit Negative")
            #! Create New Event
            if(len(forNegArray)==0):
                print('=0')
                createEventFunction(orgUnitId,xEqValue,midicaneId)
            #! Update Exsisted Event
            elif(len(forNegArray)>=1):
                print('>')
                sorted_date_array = sorted(forNegArray, key=lambda x: x['date'],reverse=True)
                # print("sorted_date_array",sorted_date_array)
                for EventJsonArray in range(len(sorted_date_array)):
                    # print(EventJsonArray)
                    print("xEqValue", xEqValue)
                    # print(sorted_date_array[EventJsonArray])
                    if(sorted_date_array[EventJsonArray]['total']==0 and sorted_date_array[EventJsonArray]['value']==0):
                        print('break == 0')
                        # sorted_date_array.pop(0)
                        continue
                    else:
                        stockbackTotal=sorted_date_array[EventJsonArray]['value']+xEqValue
                        print("stockbackTotal",stockbackTotal)
                        if(sorted_date_array[EventJsonArray]['total']==None):
                            sorted_date_array[EventJsonArray]['total']=0
                        if(sorted_date_array[EventJsonArray]['stock']==None):
                            sorted_date_array[EventJsonArray]['stock']=0
                        newEventValue=sorted_date_array[EventJsonArray]['value']+xEqValue
                        print("newEventValue", newEventValue)
                        newEventTotal=sorted_date_array[EventJsonArray]['stock']-newEventValue
                        print("newEventTotal", newEventTotal)
                        updateEventId=sorted_date_array[EventJsonArray]['event']
                        for numberOfDataElement in range(len(sorted_date_array[EventJsonArray]['query']['dataValues'])):
                            if(sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['dataElement']=='LijzB622Z22'):
                                sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['value']=newEventValue
                            if(sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['dataElement']=='bry41dJZ99x'):
                                sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['value']=newEventTotal
                        sorted_date_array[EventJsonArray]['query']['status']='ACTIVE'
                        toJsonFromEventData=json.dumps(sorted_date_array[EventJsonArray]['query'])
                        eventWithNewData=json.loads(toJsonFromEventData)
                        # print(toJsonFromEventData)
                        updateEventFunction(updateEventId,toJsonFromEventData)
                        if(stockbackTotal==0 or stockbackTotal>0):
                            print('break')
                            break
                        else:
                            if(len(sorted_date_array)<0):
                                xEqValue=stockbackTotal
                                sorted_date_array.pop(0)
                            elif(len(sorted_date_array)==0 and xEqValue < 0):
                                createEventFunction(orgUnitId,xEqValue,midicaneId)
                                xEqValue=0

# %% [markdown]
# # Running Time

# %%
print(datetime.now()-Start_DateTime)


