# Define store and update data from event to local database
import json
from ..data import check,insert_new

# This function get all new data and insert or update local database with return new object of grouping data by org and medication
def store_data(newest_data,database_connection,cursor):
        the_big_data_newest_list = []
        for numberOfNewData in range(len(newest_data)):
            new_data=newest_data[numberOfNewData]
            if(new_data['stage']=="JV6n7FhC7xp"):
                #check if this row of data exist or not
                sql = "SELECT id FROM row_data_prescribed WHERE event_id=%s AND tei = %s AND program = %s AND stage = %s AND orgUnit = %s"
                adr = (new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'])
                cursor.execute(sql, adr)
                my_result = cursor.fetchall()
                if(len(my_result)==0):
                    #if not exist insert new row to database
                    sql = "INSERT INTO row_data_prescribed (event_id,tei,program,stage,orgUnit,date,m1,q1,m2,q2,m3,q3,m4,q4,m5,q5,m6,q6,m7,q7,m8,q8,m9,q9,m10,q10,m11,q11,last_update) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
                    val = (new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'],new_data['date'], new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']),new_data['last_update'])
                    cursor.execute(sql, val)
                    database_connection.commit()
                    # print(cursor.rowcount, "record row_data_prescribed inserted.")
                else:
                    #if exist update the row
                    sql = "UPDATE row_data_prescribed SET m1=%s,q1=%s,m2=%s,q2=%s,m3=%s,q3=%s,m4=%s,q4=%s,m5=%s,q5=%s,m6=%s,q6=%s,m7=%s,q7=%s,m8=%s,q8=%s,m9=%s,q9=%s,m10=%s,q10=%s,m11=%s,q11=%s,last_update=%s WHERE event_id=%s AND tei= %s AND program= %s AND stage= %s AND orgUnit = %s"
                    val = (new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']),new_data['last_update'],new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'])
                    cursor.execute(sql, val)
                    database_connection.commit()
                    # print(cursor.rowcount, "record row_data_prescribed Updated.")
                whereQ='WHERE '+"tei= '"+ new_data['tei']+"' AND program = '"+ new_data['program']+"' AND stage = '"+ new_data['stage']+"' AND orgunit='"+ new_data['orgunit']+"'"
      
                if new_data['m1'] and new_data['q1']:
                    the_big_data_newest_list.append(insert_new(new_data['m1'],new_data['q1'],"m1",new_data))
                    whereQ=whereQ+" AND dataElement != 'm1'"
                if new_data['m2'] and new_data['q2']:
                    the_big_data_newest_list.append(insert_new(new_data['m2'], new_data['q2'],"m2",new_data))
                    whereQ=whereQ+" AND dataElement != 'm2'"
                if new_data['m3'] and new_data['q3']:
                    the_big_data_newest_list.append(insert_new(new_data['m3'], new_data['q3'],"m3",new_data))
                    whereQ=whereQ+" AND dataElement != 'm3'"
                if new_data['m4'] and new_data['q4']:
                    the_big_data_newest_list.append(insert_new(new_data['m4'], new_data['q4'],"m4",new_data))
                    whereQ=whereQ+" AND dataElement != 'm4'"
                if new_data['m5'] and new_data['q5']:
                    the_big_data_newest_list.append(insert_new(new_data['m5'], new_data['q5'],"m5",new_data))
                    whereQ=whereQ+" AND dataElement != 'm5'"
                if new_data['m6'] and new_data['q6']:
                    the_big_data_newest_list.append(insert_new(new_data['m6'], new_data['q6'],"m6",new_data))
                    whereQ=whereQ+" AND dataElement != 'm6'"
                if new_data['m7'] and new_data['q7']:
                    the_big_data_newest_list.append(insert_new(new_data['m7'], new_data['q7'],"m7",new_data))
                    whereQ=whereQ+" AND dataElement != 'm7'"
                if new_data['m8'] and new_data['q8']:
                    the_big_data_newest_list.append(insert_new(new_data['m8'], new_data['q8'],"m8",new_data))
                    whereQ=whereQ+" AND dataElement != 'm8'"
                if new_data['m9'] and new_data['q9']:
                    the_big_data_newest_list.append(insert_new(new_data['m9'], new_data['q9'],"m9",new_data))
                    whereQ=whereQ+" AND dataElement != 'm9'"
                if new_data['m10'] and new_data['q10']:
                    the_big_data_newest_list.append(insert_new(new_data['m10'], new_data['q10'],"m10",new_data))
                    whereQ=whereQ+" AND dataElement != 'm10'"
                if new_data['m11'] and new_data['q11']:
                    the_big_data_newest_list.append(insert_new(new_data['m11'], new_data['q11'],"m11",new_data))
                    whereQ=whereQ+" AND dataElement != 'm11'"
         
                
                # delete from stock data where record not equal data
                deleteQ = "DELETE FROM stock_data "+whereQ
                # print(deleteQ)
                cursor.execute(deleteQ)
                delete_result = cursor.fetchall()
                # print(len(delete_result))

            if(new_data['stage']=="tJQ1UCpkCy2"):
                # print("Frequently")
                sql = "SELECT id FROM row_data_frequently WHERE event_id = %s AND tei = %s AND program = %s AND stage = %s AND orgUnit = %s"
                adr = (new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'])
                cursor.execute(sql, adr)
                my_result = cursor.fetchall()
                if(len(my_result)==0):
                    #if not exist insert new row to database
                    sql = "INSERT INTO row_data_frequently (event_id,tei,program,stage,orgUnit,date,m1,q1,m2,q2,m3,q3,m4,q4,m5,q5,m6,q6,m7,q7,m8,q8,m9,q9,m10,q10,m11,q11,m12,q12,m13,q13,m14,q14,last_update) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'],new_data['date'], new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']),new_data['m12'], check(new_data['q12']),new_data['m13'], check(new_data['q13']),new_data['m14'], check(new_data['q14']),new_data['last_update'])
                    cursor.execute(sql, val)
                    database_connection.commit()
                    print(cursor.rowcount, "record to row_data_frequently inserted.")
                else:
                    #if exist update the row
                    sql = "UPDATE row_data_frequently SET m1=%s,q1=%s,m2=%s,q2=%s,m3=%s,q3=%s,m4=%s,q4=%s,m5=%s,q5=%s,m6=%s,q6=%s,m7=%s,q7=%s,m8=%s,q8=%s,m9=%s,q9=%s,m10=%s,q10=%s,m11=%s,q11=%s,m12=%s,q12=%s,m13=%s,q13=%s,m14=%s,q14=%s, last_update=%s WHERE event_id= %s AND tei= %s AND program= %s AND stage= %s AND orgUnit = %s"
                    val = (new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']),new_data['m12'], check(new_data['q12']),new_data['m13'], check(new_data['q13']),new_data['m14'], check(new_data['q14']),new_data['last_update'],new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'])
                    cursor.execute(sql, val)
                    database_connection.commit()
                    # print(cursor.rowcount, "record row_data_frequently Updated.")
                whereQ='WHERE '+"tei= '"+ new_data['tei']+"' AND program = '"+ new_data['program']+"' AND stage = '"+ new_data['stage']+"' AND orgunit='"+ new_data['orgunit']+"'"
    
                if new_data['m1'] and new_data['q1']:
                    the_big_data_newest_list.append(insert_new(new_data['m1'], new_data['q1'],"m1",new_data))
                    whereQ=whereQ+" AND dataElement != 'm1'"
                if new_data['m2'] and new_data['q2']:
                    the_big_data_newest_list.append(insert_new(new_data['m2'], new_data['q2'],"m2",new_data))
                    whereQ=whereQ+" AND dataElement != 'm2'"
                if new_data['m3'] and new_data['q3']:
                    the_big_data_newest_list.append(insert_new(new_data['m3'], new_data['q3'],"m3",new_data))
                    whereQ=whereQ+" AND dataElement != 'm3'"
                if new_data['m4'] and new_data['q4']:
                    the_big_data_newest_list.append(insert_new(new_data['m4'], new_data['q4'],"m4",new_data))
                    whereQ=whereQ+" AND dataElement != 'm4'"
                if new_data['m5'] and new_data['q5']:
                    the_big_data_newest_list.append(insert_new(new_data['m5'], new_data['q5'],"m5",new_data))
                    whereQ=whereQ+" AND dataElement != 'm5'"
                if new_data['m6'] and new_data['q6']:
                    the_big_data_newest_list.append(insert_new(new_data['m6'], new_data['q6'],"m6",new_data))
                    whereQ=whereQ+" AND dataElement != 'm6'"
                if new_data['m7'] and new_data['q7']:
                    the_big_data_newest_list.append(insert_new(new_data['m7'], new_data['q7'],"m7",new_data))
                    whereQ=whereQ+" AND dataElement != 'm7'"
                if new_data['m8'] and new_data['q8']:
                    the_big_data_newest_list.append(insert_new(new_data['m8'], new_data['q8'],"m8",new_data))
                    whereQ=whereQ+" AND dataElement != 'm8'"
                if new_data['m9'] and new_data['q9']:
                    the_big_data_newest_list.append(insert_new(new_data['m9'], new_data['q9'],"m9",new_data))
                    whereQ=whereQ+" AND dataElement != 'm9'"
                if new_data['m10'] and new_data['q10']:
                    the_big_data_newest_list.append(insert_new(new_data['m10'], new_data['q10'],"m10",new_data))
                    whereQ=whereQ+" AND dataElement != 'm10'"
                if new_data['m11'] and new_data['q11']:
                    the_big_data_newest_list.append(insert_new(new_data['m11'], new_data['q11'],"m11",new_data))
                    whereQ=whereQ+" AND dataElement != 'm11'"
                if new_data['m12'] and new_data['q12']:
                    the_big_data_newest_list.append(insert_new(new_data['m12'], new_data['q12'],"m12",new_data))
                    whereQ=whereQ+" AND dataElement != 'm12'"
                if new_data['m13'] and new_data['q13']:
                    the_big_data_newest_list.append(insert_new(new_data['m13'], new_data['q13'],"m13",new_data))
                    whereQ=whereQ+" AND dataElement != 'm13'"
                if new_data['m14'] and new_data['q14']:
                    the_big_data_newest_list.append(insert_new(new_data['m14'], new_data['q14'],"m14",new_data))
                    whereQ=whereQ+" AND dataElement != 'm14'"
        
                
                # delete from stock data where record not equal data
                deleteQ = "DELETE FROM stock_data "+whereQ
                cursor.execute(deleteQ)
                delete_result = cursor.fetchall()


        #GET all medicine with quantity and check on stock data (database)
        jsonStr1 = json.dumps(the_big_data_newest_list)
        for NumberOfMRecord in range(len(the_big_data_newest_list)):
            allMData =  the_big_data_newest_list[NumberOfMRecord]
            addsql = "SELECT id FROM stock_data WHERE event_id = %s AND tei = %s AND program = %s AND stage = %s AND orgUnit = %s AND dataElement = %s"
            addattr = (allMData['event_id'],allMData['tei'],allMData['program'],allMData['stage'],allMData['orgunit'],allMData['dataElement'])
            cursor.execute(addsql, addattr)
            addresult = cursor.fetchall()
            if(len(addresult)==0):
                #if not exist then insert new record 
                insSQL = "INSERT INTO stock_data (event_id,tei, program,stage, orgunit, date, dataElement, m, q) VALUES (%s ,%s , %s,%s,	%s,	%s,%s,%s,%s)"
                insVal = (allMData['event_id'],allMData['tei'], allMData['program'],allMData['stage'], allMData['orgunit'], allMData['date'], allMData['dataElement'], allMData['m'], allMData['q'])
                cursor.execute(insSQL, insVal)
                database_connection.commit()
                # print(cursor.rowcount, "record stock_data inserted.")
            else:
                #if exist then update record 
                updateSQL = "UPDATE stock_data SET m=%s, q=%s, edit_date=%s WHERE event_id = %s AND tei= %s AND program= %s AND stage= %s AND orgUnit = %s AND dataElement = %s"
                updateVal = (allMData['m'],allMData['q'],allMData['edit_date'],allMData['event_id'],allMData['tei'],allMData['program'],allMData['stage'],allMData['orgunit'],allMData['dataElement'])
                cursor.execute(updateSQL, updateVal)
                database_connection.commit()
                # print(cursor.rowcount, "record stock_data Updated.")
        #select and store all stock data by medicine and orgunit
        sumQ = "SELECT orgunit,m,SUM(q) AS q FROM stock_data GROUP BY m,orgunit"
        cursor.execute(sumQ)
        sumResult = cursor.fetchall()
        mydict = []
        # print(sumResult)
        for row in sumResult:
            mydict.append({"orgunit":row[0],"m":row[1],"q":str(row[2])})
        stud_json = json.dumps(mydict)
        return stud_json

