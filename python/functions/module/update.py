import json




def updateData(stud_json):
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
                            # print("in")
                            activeEventArray.append({"event":eventArray['event'],"date":datetime. strptime(eventArray['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"value":eventValue,"total":totalValue,"query":eventArray})
                            forNegArray.append({"event":eventArray['event'],"date":datetime. strptime(eventArray['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"stock":eventTotalValue,"value":eventValue,"total":totalValue,"query":eventArray})
                        else:
                            # print("out")
                            datexxx=datetime. strptime(eventArray['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date() if eventArray['eventDate']!=None else ''
                            notActiveEventArray.append({"event":datexxx ,"date":datetime. strptime(eventArray['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"stock":eventTotalValue,"value":eventValue,"total":totalValue,"query":eventArray})
                            forNegArray.append({"event":eventArray['event'],"date":datetime. strptime(eventArray['eventDate'], '%Y-%m-%dT%H:%M:%S.%f').date(),"stock":eventTotalValue,"value":eventValue,"total":totalValue,"query":eventArray})
            else:
                print("Equal Zero")


    #Start Update on DHIS2
    #?? No Edit Senario
            if(xEqValue==0):
                print("No Edit")
    #?? Positive Senario
            elif( xEqValue>0):
                print("Edit Positive")
                #! Create New Event
                if(len(activeEventArray)==0):
                    print('=0')
                    createEventFunction(orgUnitId,xEqValue,midicaneId)
                #! Update Exsisted Event
                elif(len(activeEventArray)>0):
                    positiveTotal=False
                    queryValue=0
                    queryStock=0
                    queryTotal=0
                    quantityStockSelected=0
                    newEventValue=0
                    quantityStockSelected=0
                    print('>')
                    sorted_date_array = sorted(activeEventArray, key=lambda x: x['date'])
                    swapArray=sorted_date_array[0]['total']
                    eventSelectID=''
                    #loop on all event to check if we have good total or >0
                    for EventJsonArray in range(len(sorted_date_array)):
                        if  sorted_date_array[EventJsonArray]['total'] >= swapArray:
                            if(sorted_date_array[EventJsonArray]['total']>0):
                                positiveTotal=True
                            swapArray= sorted_date_array[EventJsonArray]['total']
                            eventSelectID=sorted_date_array[EventJsonArray]['event']
                    if(positiveTotal):
                            selectedData=list(filter(lambda x:x["event"]==eventSelectID,sorted_date_array))
                            updateEventId=selectedData[0]['event']

                            for numberOfDataElement in range(len(selectedData[0]['query']['dataValues'])):
                                if(selectedData[0]['query']['dataValues'][numberOfDataElement]['dataElement']=='LijzB622Z22'):
                                        queryValue=int(selectedData[0]['query']['dataValues'][numberOfDataElement]['value'])
                                if(selectedData[0]['query']['dataValues'][numberOfDataElement]['dataElement']=='eskqGfai0gc'):
                                        queryStock=int(selectedData[0]['query']['dataValues'][numberOfDataElement]['value'])
                                if(selectedData[0]['query']['dataValues'][numberOfDataElement]['dataElement']=='bry41dJZ99x'):
                                        queryTotal=int(selectedData[0]['query']['dataValues'][numberOfDataElement]['value'])
        
                            #Calculate new values
                            if(abs(xEqValue)>queryTotal):
                                xEqValue=xEqValue-queryTotal
                                newEventValue= queryTotal+xEqValue
                                print("xEqValue",xEqValue)
                                print("newEventValue",newEventValue)
                            else:
                                newEventValue=queryValue+xEqValue
                                queryTotal=queryStock-newEventValue
                                xEqValue=0


                            for numberOfDataElement in range(len(selectedData[0]['query']['dataValues'])):
                                if(selectedData[0]['query']['dataValues'][numberOfDataElement]['dataElement']=='LijzB622Z22'):
                                    selectedData[0]['query']['dataValues'][numberOfDataElement]['value']=newEventValue
                                if(selectedData[0]['query']['dataValues'][numberOfDataElement]['dataElement']=='bry41dJZ99x'):
                                        selectedData[0]['query']['dataValues'][numberOfDataElement]['value']=queryTotal
                            #update on DHIS2
                            toJsonFromEventData=json.dumps(selectedData[0]['query'])
                            eventWithNewData=json.loads(toJsonFromEventData)
                            del eventWithNewData["href"]
                            del eventWithNewData['deleted']
                            del eventWithNewData['notes']
                            del eventWithNewData['lastUpdated']
                            del eventWithNewData['eventDate']
                            del eventWithNewData['dueDate']
                            toJsonFormat=json.dumps(eventWithNewData)
                            updateEventFunction(updateEventId,toJsonFormat)
                    else:
                        # No Array have Total above 0 >>0 :: select fist one and add the value on it
                        selectedData=sorted_date_array[0]
                        updateEventId=sorted_date_array[0]['event']
                        for numberOfDataElement in range(len(sorted_date_array[0]['query']['dataValues'])):
                            if(sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['dataElement']=='LijzB622Z22'):
                                newEventValue=int(sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['value'])+xEqValue
                                sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['value']= int(sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['value'])+xEqValue
                            if(sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['dataElement']=='LCWyFX0sjqM'):
                                quantityStockSelected=sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['value']
                            if(sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['dataElement']=='bry41dJZ99x'):
                                sorted_date_array[0]['query']['dataValues'][numberOfDataElement]['value']=quantityStockSelected-newEventValue
                        toJsonFromEventData=json.dumps(sorted_date_array[0]['query'])
                        eventWithNewData=json.loads(toJsonFromEventData)
                        del eventWithNewData["href"]
                        del eventWithNewData['deleted']
                        del eventWithNewData['notes']
                        del eventWithNewData['lastUpdated']
                        del eventWithNewData['eventDate']
                        del eventWithNewData['dueDate']
                        toJsonFormat=json.dumps(eventWithNewData)
                        updateEventFunction(updateEventId,toJsonFormat)
                        # xEqValue=0
                    if(xEqValue==0):
                        print('break')
                        break
                    else:
                        if(len(activeEventArray)>0):
                            # xEqValue=newEventValue
                            activeEventArray.pop(0)
                            if(len(activeEventArray)==0 and xEqValue !=0):
                                createEventFunction(orgUnitId,xEqValue,midicaneId)
                                xEqValue=0
    #?? Negative Senario
            elif(xEqValue<0):
                # print(forNegArray)
                print("Edit Negative")
                #! Create New Event
                if(len(forNegArray)==0):
                    print('=0')
                    createEventFunction(orgUnitId,xEqValue,midicaneId)
                elif(len(forNegArray)>=1):
                    print('>')
                    sorted_date_array = sorted(forNegArray, key=lambda x: x['date'],reverse=True)
                    # print("sorted_date_array",sorted_date_array)
                    for EventJsonArray in range(len(sorted_date_array)):
                        # print("xEqValue", xEqValue)
                        if(sorted_date_array[EventJsonArray]['total']==0 and sorted_date_array[EventJsonArray]['value']==0):
                            print('break == 0')
                            # sorted_date_array.pop(0)
                            continue
                        else:
                            newEventTotal=0
                            if(abs(xEqValue)>sorted_date_array[EventJsonArray]['value']):
                                newEventValue=0
                                xEqValue=sorted_date_array[EventJsonArray]['value']+xEqValue
                            else:
                                newEventValue=sorted_date_array[EventJsonArray]['value']+xEqValue
                                xEqValue=0
                            if(sorted_date_array[EventJsonArray]['total']==None):
                                sorted_date_array[EventJsonArray]['total']=0
                            if(sorted_date_array[EventJsonArray]['stock']==None):
                                sorted_date_array[EventJsonArray]['stock']=0
                            updateEventId=sorted_date_array[EventJsonArray]['event']
                            for numberOfDataElement in range(len(sorted_date_array[EventJsonArray]['query']['dataValues'])):
                                if(sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['dataElement']=='LijzB622Z22'):
                                    sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['value']=newEventValue
                                if(sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['dataElement']=='LCWyFX0sjqM'):
                                    newEventTotal=sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['value']
                                if(sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['dataElement']=='bry41dJZ99x'):
                                    sorted_date_array[EventJsonArray]['query']['dataValues'][numberOfDataElement]['value']=newEventTotal-newEventValue
                            #store Evend it
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
                            updateEventFunction(updateEventId,toJsonFormat)
                            if(xEqValue==0 or xEqValue>0):
                                print('break')
                                break
                            else:
                                if(len(sorted_date_array)<0):
                                    sorted_date_array.pop(0)
                                elif(len(sorted_date_array)==0 and xEqValue < 0):
                                    createEventFunction(orgUnitId,xEqValue,midicaneId)
                                    xEqValue=0
