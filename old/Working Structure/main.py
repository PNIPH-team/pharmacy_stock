# Import Library #
import json
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from datetime import date
from datetime import datetime
import os

if __name__ == '__main__':
    # Create Today File #
    # Main Variable #
    categoryOptionsList = []
    today = date.today()
    newest_data = []
    Start_DateTime = datetime.now()
    print(Start_DateTime)
    today_date = today.strftime("%Y-%m-%d")
    todayDateTime = "LOG/Stock_" + str(datetime.now())
    path = '/Users/salehabbas/Developer/Python/pharmacy_stock/' + \
        todayDateTime
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)

# Public Functions #
    def writefile(FileName, Data):
        json_data = json.dumps(Data, ensure_ascii=False)
        file = open(FileName, "w")
        with open(file.name, "w") as f:
            f.write(json_data)
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
        for h in args:
            categoryOptionsList.append(h)

    if not os.path.exists('categoryOptions.json'):
        category_options()
# Get All category Option Function #
    print("--------------------------------Start Loop--------------------------------")

    get_org_unit_req = requests.get(
        "https://hmis.moh.ps/tr-dev/api/programs/fnIEoaflGxX?fields=organisationUnits",
        auth=HTTPBasicAuth('Saleh', 'Test@123'))
    get_org_unit_data = json.loads(get_org_unit_req.text)
    for u in range(len(get_org_unit_data['organisationUnits'])):
        org_unit_id = get_org_unit_data['organisationUnits'][u]['id']
        # ? print(get_org_unit_data['organisationUnits'][u]['id'])

        get_tei = requests.get(
            "https://hmis.moh.ps/tr-dev/api/trackedEntityInstances?ou=" +
            org_unit_id+"&fields=trackedEntityInstance&lastUpdatedEndDate="
            + today_date + "&lastUpdatedStartDate=" + today_date,
            auth=HTTPBasicAuth('Saleh', 'Test@123'))
        get_tei_data = json.loads(get_tei.text)
        # ? print(get_tei_data)
        for i in range(len(get_tei_data['trackedEntityInstances'])):
            loop_array = {"tei": "", "event": "", "orgunit": "", "date": "", "m": "", "q": "", "m1": "", "q1": "", "m2": "",
                          "q2": "", "m3": "", "q3": "",
                          "m4": "", "q4": "", "m5": "", "q5": "", "m6": "", "q6": "", "m7": "", "q7": "", "m8": "",
                          "q8": "", "m9": "", "q9": "", "m10": "", "q10": ""}
            tei_id = get_tei_data['trackedEntityInstances'][i]['trackedEntityInstance']
            # ? print("tei_id= "+tei_id)
            loop_array['tei'] = tei_id
            get_event = requests.get(
                "https://hmis.moh.ps/tr-dev/api/events?trackedEntityInstance=" + tei_id + "&lastUpdatedEndDate=" +
                today_date + "&lastUpdatedStartDate=" + today_date + "&fields=event,orgUnit",
                auth=HTTPBasicAuth('Saleh', 'Test@123'))
            get_event_data = json.loads(get_event.text)

            for j in range(len(get_event_data['events'])):
                event_id = get_event_data['events'][j]['event']
                orgunit = get_event_data['events'][j]['orgUnit']
                loop_array['event'] = event_id
                loop_array['orgunit'] = orgunit
                loop_array['date'] = today_date
                # ? print("event_id= "+event_id)
                get_event_id = requests.get(
                    "https://hmis.moh.ps/tr-dev/api/events/" + event_id, auth=HTTPBasicAuth('Saleh', 'Test@123'))
                get_event_id_data = json.loads(get_event_id.text)
                # ? print(len(get_event_id_data['dataValues']) == 0)
                if('dataValues' in json.dumps(get_event_id_data)):
                    for k in range(len(get_event_id_data['dataValues'])):
                        loop_array['event'] = event_id
                        event_id_data = get_event_id_data['dataValues'][k]['dataElement']
                        dataelement_date = datetime.strptime(
                            (get_event_id_data['dataValues'][k]['created'])[0:10], '%Y-%m-%d').strftime("%Y-%m-%d")
                        # ? print(dataelement_date)
                        if today_date == dataelement_date:
                            # ? Store All M Values From Event DataElement
                            if event_id_data == "aM2Vn0UUPJB":
                                event_value = get_event_id_data['dataValues'][k]['value']
                                loop_array['m'] = event_value
                            if event_id_data == "WSeukMBwbQ3":
                                event_value = get_event_id_data['dataValues'][k]['value']
                                loop_array['m1'] = event_value
                            if event_id_data == "TORfS27wR0q":
                                event_value = get_event_id_data['dataValues'][k]['value']
                                loop_array['m2'] = event_value
                            if event_id_data == "TnrWDEL4PoR":
                                event_value = get_event_id_data['dataValues'][k]['value']
                                loop_array['m3'] = event_value
                            if event_id_data == "iy166uomfXk":
                                event_value = get_event_id_data['dataValues'][k]['value']
                                loop_array['m4'] = event_value
                            if event_id_data == "ntECq4xEo24":
                                event_value = get_event_id_data['dataValues'][k]['value']
                                loop_array['m5'] = event_value
                            if event_id_data == "Ne2veOUhPw0":
                                event_value = get_event_id_data['dataValues'][k]['value']
                                loop_array['m6'] = event_value
                            if event_id_data == "R2rxr1Z8i4v":
                                event_value = get_event_id_data['dataValues'][k]['value']
                                loop_array['m7'] = event_value
                            if event_id_data == "Dlx79ePwf1g":
                                event_value = get_event_id_data['dataValues'][k]['value']
                                loop_array['m8'] = event_value
                            if event_id_data == "oTCRn8enMzd":
                                event_value = get_event_id_data['dataValues'][k]['value']
                                loop_array['m9'] = event_value
                            if event_id_data == "nTd67mb0PJe":
                                event_value = get_event_id_data['dataValues'][k]['value']
                                loop_array['m10'] = event_value
                        # ? Store All Q Values From Event DataElement
                            if event_id_data == "HS5mppnnRUD":
                                event_value = int(
                                    get_event_id_data['dataValues'][k]['value'])
                                loop_array['q'] = event_value
                            if event_id_data == "Kzxa8SKjCdp":
                                event_value = int(
                                    get_event_id_data['dataValues'][k]['value'])
                                loop_array['q1'] = event_value
                            if event_id_data == "wmkND48fkvf":
                                event_value = int(
                                    get_event_id_data['dataValues'][k]['value'])
                                loop_array['q2'] = event_value
                            if event_id_data == "sm78nae74E0":
                                event_value = int(
                                    get_event_id_data['dataValues'][k]['value'])
                                loop_array['q3'] = event_value
                            if event_id_data == "YR7bARfLBay":
                                event_value = int(
                                    get_event_id_data['dataValues'][k]['value'])
                                loop_array['q4'] = event_value
                            if event_id_data == "Pl3jCeEVYVG":
                                event_value = int(
                                    get_event_id_data['dataValues'][k]['value'])
                                loop_array['q5'] = event_value
                            if event_id_data == "J6s8Ju9Y1xk":
                                event_value = int(
                                    get_event_id_data['dataValues'][k]['value'])
                                loop_array['q6'] = event_value
                            if event_id_data == "xFAUNJilvDg":
                                event_value = int(
                                    get_event_id_data['dataValues'][k]['value'])
                                loop_array['q7'] = event_value
                            if event_id_data == "tn3XjDR6aUt":
                                event_value = int(
                                    get_event_id_data['dataValues'][k]['value'])
                                loop_array['q8'] = event_value
                            if event_id_data == "H2g1tcKI0sK":
                                event_value = int(
                                    get_event_id_data['dataValues'][k]['value'])
                                loop_array['q9'] = event_value
                            if event_id_data == "wFeFcxSnOO0":
                                event_value = int(
                                    get_event_id_data['dataValues'][k]['value'])
                                loop_array['q10'] = event_value
                newest_data.append(loop_array)
# Store Data Togather
    print("--------------------------------Store Data Togather--------------------------------")

    if not len(newest_data) == 0:
        jsonStr = json.dumps(newest_data)
        writefile(todayDateTime + "/RowData_" +
                  today_date + ".json", json.loads(jsonStr))
        the_big_data_newest_list = []
        for a in range(len(newest_data)):
            def InsertNew(mvalue, qvalue):
                the_big_data_array = {"tei": newest_data[a]['tei'], "event": newest_data[a]['event'],
                                      "orgunit": newest_data[a]['orgunit'], "date": newest_data[a]['date'], "m": mvalue,
                                      "q": qvalue}
                the_big_data_newest_list.append(the_big_data_array)

            if newest_data[a]['m'] and newest_data[a]['q']:
                InsertNew(newest_data[a]['m'], newest_data[a]['q'])
            if newest_data[a]['m1'] and newest_data[a]['q1']:
                InsertNew(newest_data[a]['m1'], newest_data[a]['q1'])
            if newest_data[a]['m2'] and newest_data[a]['q2']:
                InsertNew(newest_data[a]['m2'], newest_data[a]['q2'])
            if newest_data[a]['m3'] and newest_data[a]['q3']:
                InsertNew(newest_data[a]['m3'], newest_data[a]['q3'])
            if newest_data[a]['m4'] and newest_data[a]['q4']:
                InsertNew(newest_data[a]['m4'], newest_data[a]['q4'])
            if newest_data[a]['m5'] and newest_data[a]['q5']:
                InsertNew(newest_data[a]['m5'], newest_data[a]['q5'])
            if newest_data[a]['m6'] and newest_data[a]['q6']:
                InsertNew(newest_data[a]['m6'], newest_data[a]['q6'])
            if newest_data[a]['m7'] and newest_data[a]['q7']:
                InsertNew(newest_data[a]['m7'], newest_data[a]['q7'])
            if newest_data[a]['m8'] and newest_data[a]['q8']:
                InsertNew(newest_data[a]['m8'], newest_data[a]['q8'])
            if newest_data[a]['m9'] and newest_data[a]['q9']:
                InsertNew(newest_data[a]['m9'], newest_data[a]['q9'])
            if newest_data[a]['m10'] and newest_data[a]['q10']:
                InsertNew(newest_data[a]['m10'], newest_data[a]['q10'])
        jsonStr1 = json.dumps(the_big_data_newest_list)
        # ? print(jsonStr1)
#### GroupBy M And OrgUnit With Some q ####
        print("--------------------------------GroupBy--------------------------------")
        df = pd.DataFrame(json.loads(jsonStr1))
        groupby_values = df.groupby(['m', 'orgunit'])['q'].sum()
        js = groupby_values.to_json(orient='table')
        # ? print(json.loads(js))
        writefile(todayDateTime + "/GroupData_" +
                  today_date + ".json", json.loads(js))

# Mapping M With M Code #
        print("--------------------------------Mapping And Store attributeCategoryOptions--------------------------------")

        def MappingData():
            NewMappingArray = []
            with open('categoryOptions.json') as f1, open(todayDateTime + "/GroupData_" + today_date + ".json") as f2:
                a = json.load(f1)
                b = json.load(f2)
                for c in range(len(b['data'])):
                    mCode = ""
                    OrgUnit_fromjson = b['data'][c]['orgunit']
                    quantity_fromjson = b['data'][c]['q']
                    mName = b['data'][c]['m']
                    for v in range(len(a)):
                        if a[v]['code'] == mName:
                            mCode = a[v]['id']
                            newArray = {"orgunit": OrgUnit_fromjson,
                                        "mCode": mCode, "quantity": quantity_fromjson}
                            NewMappingArray.append(newArray)
                if len(b['data']) != len(NewMappingArray):
                    category_options()
                    MappingData()
                else:
                    jsonArrayMapping = json.dumps(NewMappingArray)
                    MappingDataArray = json.loads(jsonArrayMapping)
                    writefile(todayDateTime + "/GroupData_Mapping_" + today_date +
                              ".json", MappingDataArray)
            return MappingDataArray

        MappingDataArray = MappingData()
        # ? print(MappingDataArray)
        xxxxxxx = json.dumps(MappingDataArray)
        # ? print(xxxxxxx)
        salehh = pd.DataFrame(json.loads(xxxxxxx))
        # ? print(salehh)
        fzfzf = salehh.groupby(salehh['orgunit']).sum()
        # ? print(fzfzf)
        newJsonOrgUnit = fzfzf.to_json(orient='table')
        ccoa = json.loads(newJsonOrgUnit)
        att_array = []
        attribute_json = []
        for y in range(len(ccoa['data'])):
            # ? print(ccoa['data'][y]['orgunit'])
            org_in_array = ccoa['data'][y]['orgunit']
### Store all attributeCategoryOptions Data From API ####
            att_req = requests.get(
                "https://hmis.moh.ps/tr-dev/api/events?fields=attributeCategoryOptions,event,lastUpdated&orgUnit=" +
                org_in_array+"&program=fnIEoaflGxX",
                auth=HTTPBasicAuth('Saleh', 'Test@123'))
            att_req_data = json.loads(att_req.text)

            for m in range(len(att_req_data['events'])):
                if att_req_data['events'][m]['attributeCategoryOptions'] not in att_array:
                    att_array.append(att_req_data['events']
                                     [m]['attributeCategoryOptions'])
                    attribute_json.append({"event": att_req_data['events'][m]['event'], "lastUpdated": att_req_data['events']
                                           [m]['lastUpdated'], "attributeCategoryOptions": att_req_data['events'][m]['attributeCategoryOptions']})
                elif att_req_data['events'][m]['attributeCategoryOptions'] in att_array:
                    # ? print(att_req_data['events'][m]['lastUpdated'])
                    # ? print(att_array)

                    # a-> in list
                    a_list = [a['lastUpdated'] for a in attribute_json if a['attributeCategoryOptions']
                              == att_req_data['events'][m]['attributeCategoryOptions']]
                    var_a = a_list[0]
                    # b-> new one
                    var_b = att_req_data['events'][m]['lastUpdated']
                    # ?print(var_a)
                    # ?print(att_req_data['events'][m] ['attributeCategoryOptions'])
                    # ?print(var_b)
                    # ? change to >
                    if var_b > var_a:
                        for a in attribute_json:
                            print(attribute_json)
                            if a['attributeCategoryOptions'] == att_req_data['events'][m]['attributeCategoryOptions']:
                                a['event'] = att_req_data['events'][m]['event']
                                a['lastUpdated'] = att_req_data['events'][m]['lastUpdated']
                            for fgtr in range(len(att_array)):
                                print(att_array[fgtr])
                                if(att_array[fgtr] == a['attributeCategoryOptions']):
                                    att_array[fgtr] = att_req_data['events'][m]['attributeCategoryOptions']
                                    print(att_array[fgtr])
        # print(att_array)
        # ? print(attribute_json)
#### Multiple Loop to check if event exist or not ####
        # ? print(MappingDataArray)
        Update_response_array = []
        Create_response_array = []
        print("--------------------------------Update Data Stage--------------------------------")
        for p in range(len(MappingDataArray)):
            mappingArrayCode = MappingDataArray[p]['mCode']
            mappingArrayorgunit = MappingDataArray[p]['orgunit']
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
                headers = {'Content-Type': 'application/json'}
                create_event = requests.post("https://hmis.moh.ps/tr-dev/api/events",
                                             data=json.dumps(data), headers=headers, auth=HTTPBasicAuth('Saleh', 'Test@123'))
                att_req_data = json.loads(create_event.text)
                Create_response_array.append(att_req_data)
                print("Create Stock Successfully")
            elif(mappingArrayCode in att_array):
                for t in range(len(attribute_json)):
                    if(attribute_json[t]['attributeCategoryOptions'] == mappingArrayCode):
                        storeEventId = attribute_json[t]['event']
                # get every event q value and add this value to it
                        event_req = requests.get(
                            "https://hmis.moh.ps/tr-dev/api/events/"+storeEventId, auth=HTTPBasicAuth('Saleh', 'Test@123'))
                        selected_event_data = json.loads(event_req.text)
                        for r in range(len(selected_event_data['dataValues'])):
                            if(selected_event_data['dataValues'][r]['dataElement'] == 'LijzB622Z22'):
                                old_q_value = int(
                                    selected_event_data['dataValues'][r]['value'])
                                new_q_value = int(
                                    MappingDataArray[p]['quantity'])
                                sum_value = old_q_value+new_q_value
                                selected_event_data['dataValues'][r]['value'] = sum_value
                                data = json.dumps(selected_event_data)
                                headers = {'Content-Type': 'application/json'}
                                Update_req = requests.put(
                                    "https://hmis.moh.ps/tr-dev/api/events/"+storeEventId, data=data, headers=headers, auth=HTTPBasicAuth('Saleh', 'Test@123'))
                                Update_response = json.loads(Update_req.text)
                                Update_response_array.append(Update_response)
                                print("Update Stock Successfully")
    writefile(todayDateTime+"/Update_ImportSummaries_" +
              today_date+".json", Update_response_array)
    writefile(todayDateTime+"/Create_ImportSummaries_" +
              today_date+".json", att_req_data)
print(datetime.now()-Start_DateTime)
