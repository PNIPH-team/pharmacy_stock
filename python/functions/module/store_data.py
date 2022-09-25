import json
# from ..connect_database import connect_database,query
from ..data import check,insert_new


def store_data(newest_data,database_connection,cursor):
        the_big_data_newest_list = []
        for numberOfNewData in range(len(newest_data)):
            new_data=newest_data[numberOfNewData]
            if(new_data['stage']=="JV6n7FhC7xp"):
                print("Prescribed")
                #check if this row of data exist or not
                sql = "SELECT id FROM row_data_prescribed WHERE tei = %s AND program = %s AND stage = %s AND orgUnit = %s"
                adr = (new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'])
                cursor.execute(sql, adr)
                my_result = cursor.fetchall()
                if(len(my_result)==0):
                    print(new_data)
                    #if not exist insert new row to database
                    sql = "INSERT INTO row_data_prescribed (tei,program,stage,orgUnit,date,m1,q1,m2,q2,m3,q3,m4,q4,m5,q5,m6,q6,m7,q7,m8,q8,m9,q9,m10,q10,m11,q11,last_update) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
                    val = (new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'],new_data['date'], new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']),new_data['last_update'])
                    cursor.execute(sql, val)
                    database_connection.commit()
                    print(cursor.rowcount, "record inserted.")
                else:
                    #if exist update the row
                    sql = "UPDATE row_data_prescribed SET m1=%s,q1=%s,m2=%s,q2=%s,m3=%s,q3=%s,m4=%s,q4=%s,m5=%s,q5=%s,m6=%s,q6=%s,m7=%s,q7=%s,m8=%s,q8=%s,m9=%s,q9=%s,m10=%s,q10=%s,m11=%s,q11=%s,m12=%s,q12=%s,m13=%s,q13=%s,m14=%s,q14=%s,m15=%s,q15=%s,m16=%s,q16=%s,m17=%s,q17=%s,m18=%s,q18=%s,m19=%s,q19=%s,m20=%s,q20=%s,m21=%s,q21=%s,m22=%s,q22=%s,m23=%s,q23=%s,m24=%s,q24=%s , last_update=%s WHERE tei= %s AND program= %s AND stage= %s AND orgUnit = %s"
                    val = (new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']),new_data['last_update'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'])
                    cursor.execute(sql, val)
                    database_connection.commit()
                    print(cursor.rowcount, "record Updated.")
                whereQ='WHERE '+"tei= '"+ new_data['tei']+"' AND program = '"+ new_data['program']+"' AND stage = '"+ new_data['stage']+"' AND orgunit='"+ new_data['orgunit']+"'"
      
                if new_data['m1'] and new_data['q1']:
                    insert_new(new_data['m1'], new_data['q1'],"m1")
                    whereQ=whereQ+" AND dataElement != 'm1'"
                if new_data['m2'] and new_data['q2']:
                    insert_new(new_data['m2'], new_data['q2'],"m2")
                    whereQ=whereQ+" AND dataElement != 'm2'"
                if new_data['m3'] and new_data['q3']:
                    insert_new(new_data['m3'], new_data['q3'],"m3")
                    whereQ=whereQ+" AND dataElement != 'm3'"
                if new_data['m4'] and new_data['q4']:
                    insert_new(new_data['m4'], new_data['q4'],"m4")
                    whereQ=whereQ+" AND dataElement != 'm4'"
                if new_data['m5'] and new_data['q5']:
                    insert_new(new_data['m5'], new_data['q5'],"m5")
                    whereQ=whereQ+" AND dataElement != 'm5'"
                if new_data['m6'] and new_data['q6']:
                    insert_new(new_data['m6'], new_data['q6'],"m6")
                    whereQ=whereQ+" AND dataElement != 'm6'"
                if new_data['m7'] and new_data['q7']:
                    insert_new(new_data['m7'], new_data['q7'],"m7")
                    whereQ=whereQ+" AND dataElement != 'm7'"
                if new_data['m8'] and new_data['q8']:
                    insert_new(new_data['m8'], new_data['q8'],"m8")
                    whereQ=whereQ+" AND dataElement != 'm8'"
                if new_data['m9'] and new_data['q9']:
                    insert_new(new_data['m9'], new_data['q9'],"m9")
                    whereQ=whereQ+" AND dataElement != 'm9'"
                if new_data['m10'] and new_data['q10']:
                    insert_new(new_data['m10'], new_data['q10'],"m10")
                    whereQ=whereQ+" AND dataElement != 'm10'"
                if new_data['m11'] and new_data['q11']:
                    insert_new(new_data['m11'], new_data['q11'],"m11")
                    whereQ=whereQ+" AND dataElement != 'm11'"
         
                
                # delete from stock data where record not equal data
                deleteQ = "DELETE FROM stock_data "+whereQ
                print(deleteQ)
                cursor.execute(deleteQ)
                delete_result = cursor.fetchall()
                print(len(delete_result))

            if(new_data['stage']=="tJQ1UCpkCy2"):
                print("Frequently")



















            #check if this row of data exist or not
            # sql = "SELECT id FROM RowData WHERE tei = %s AND program = %s AND orgUnit = %s"
            # adr = (new_data['tei'],new_data['program'],new_data['orgunit'])
            # connect_database.cursor().execute(sql, adr)
            # my_result = connect_database.cursor().fetchall()
            # if(len(my_result)==0):
            #     #if not exist insert new row to database
            #     sql = "INSERT INTO RowData (tei,program,orgUnit,date,	m,	q,	m1,	q1,	m2,	q2,	m3,	q3,	m4,	q4,	m5,	q5,	m6,	q6,	m7,	q7,	m8,	q8,	m9,	q9,	m10,	q10,	m11,	q11,	m12,	q12,	m13,	q13,	m14,	q14,	m15,	q15,	m16,	q16,	m17,	q17,	m18,	q18,	m19,	q19,	m20,	q20,	m21,	q21,	m22,	q22,	m23,	q23,	m24,	q24,last_update) VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s)"
            #     val = (new_data['tei'],new_data['program'],new_data['orgunit'],new_data['date'],new_data['m'], check(new_data['q']), new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']), new_data['m12'], check(new_data['q12']), new_data['m13'], check(new_data['q13']), new_data['m14'], check(new_data['q14']), new_data['m15'], check(new_data['q15']), new_data['m16'], check(new_data['q16']), new_data['m17'], check(new_data['q17']), new_data['m18'], check(new_data['q18']), new_data['m19'], check(new_data['q19']), new_data['m20'], check(new_data['q20']), new_data['m21'], check(new_data['q21']), new_data['m22'], check(new_data['q22']), new_data['m23'], check(new_data['q23']), new_data['m24'], check(new_data['q24']),new_data['last_update'])
            #     connect_database.cursor().execute(sql, val)
            #     connect_database.commit()
            #     print(connect_database.cursor().rowcount, "record inserted.")
            # else:
            #     #if exist update the row
            #     sql = "UPDATE RowData SET m=%s,q=%s,m1=%s,q1=%s,m2=%s,q2=%s,m3=%s,q3=%s,m4=%s,q4=%s,m5=%s,q5=%s,m6=%s,q6=%s,m7=%s,q7=%s,m8=%s,q8=%s,m9=%s,q9=%s,m10=%s,q10=%s,m11=%s,q11=%s,m12=%s,q12=%s,m13=%s,q13=%s,m14=%s,q14=%s,m15=%s,q15=%s,m16=%s,q16=%s,m17=%s,q17=%s,m18=%s,q18=%s,m19=%s,q19=%s,m20=%s,q20=%s,m21=%s,q21=%s,m22=%s,q22=%s,m23=%s,q23=%s,m24=%s,q24=%s , last_update=%s WHERE tei= %s AND program= %s AND orgUnit = %s"
            #     val = (new_data['m'], check(new_data['q']), new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']), new_data['m12'], check(new_data['q12']), new_data['m13'], check(new_data['q13']), new_data['m14'], check(new_data['q14']), new_data['m15'], check(new_data['q15']), new_data['m16'], check(new_data['q16']), new_data['m17'], check(new_data['q17']), new_data['m18'], check(new_data['q18']), new_data['m19'], check(new_data['q19']), new_data['m20'], check(new_data['q20']), new_data['m21'], check(new_data['q21']), new_data['m22'], check(new_data['q22']), new_data['m23'], check(new_data['q23']), new_data['m24'], check(new_data['q24']),new_data['last_update'],new_data['tei'],new_data['program'],new_data['orgunit'])
            #     connect_database.cursor().execute(sql, val)
            #     connect_database.commit()
            #     print(connect_database.cursor().rowcount, "record Updated.")
            # whereQ='WHERE '+"tei= '"+ new_data['tei']+"' AND program = '"+ new_data['program']+"' AND orgunit='"+ new_data['orgunit']+"'"
            # if new_data['m'] and new_data['q']:
            #     insert_new(new_data['m'], new_data['q'],"m")
            #     whereQ=whereQ+" AND dataElement != 'm'"
            # if new_data['m1'] and new_data['q1']:
            #     insert_new(new_data['m1'], new_data['q1'],"m1")
            #     whereQ=whereQ+" AND dataElement != 'm1'"
            # if new_data['m2'] and new_data['q2']:
            #     insert_new(new_data['m2'], new_data['q2'],"m2")
            #     whereQ=whereQ+" AND dataElement != 'm2'"
            # if new_data['m3'] and new_data['q3']:
            #     insert_new(new_data['m3'], new_data['q3'],"m3")
            #     whereQ=whereQ+" AND dataElement != 'm3'"
            # if new_data['m4'] and new_data['q4']:
            #     insert_new(new_data['m4'], new_data['q4'],"m4")
            #     whereQ=whereQ+" AND dataElement != 'm4'"
            # if new_data['m5'] and new_data['q5']:
            #     insert_new(new_data['m5'], new_data['q5'],"m5")
            #     whereQ=whereQ+" AND dataElement != 'm5'"
            # if new_data['m6'] and new_data['q6']:
            #     insert_new(new_data['m6'], new_data['q6'],"m6")
            #     whereQ=whereQ+" AND dataElement != 'm6'"
            # if new_data['m7'] and new_data['q7']:
            #     insert_new(new_data['m7'], new_data['q7'],"m7")
            #     whereQ=whereQ+" AND dataElement != 'm7'"
            # if new_data['m8'] and new_data['q8']:
            #     insert_new(new_data['m8'], new_data['q8'],"m8")
            #     whereQ=whereQ+" AND dataElement != 'm8'"
            # if new_data['m9'] and new_data['q9']:
            #     insert_new(new_data['m9'], new_data['q9'],"m9")
            #     whereQ=whereQ+" AND dataElement != 'm9'"
            # if new_data['m10'] and new_data['q10']:
            #     insert_new(new_data['m10'], new_data['q10'],"m10")
            #     whereQ=whereQ+" AND dataElement != 'm10'"
            # if new_data['m11'] and new_data['q11']:
            #     insert_new(new_data['m11'], new_data['q11'],"m11")
            #     whereQ=whereQ+" AND dataElement != 'm11'"
            # if new_data['m12'] and new_data['q12']:
            #     insert_new(new_data['m12'], new_data['q12'],"m12")
            #     whereQ=whereQ+" AND dataElement != 'm12'"
            # if new_data['m13'] and new_data['q13']:
            #     insert_new(new_data['m13'], new_data['q13'],"m13")
            #     whereQ=whereQ+" AND dataElement != 'm13'"
            # if new_data['m14'] and new_data['q14']:
            #     insert_new(new_data['m14'], new_data['q14'],"m14")
            #     whereQ=whereQ+" AND dataElement != 'm14'"
            # if new_data['m15'] and new_data['q15']:
            #     insert_new(new_data['m15'], new_data['q15'],"m15")
            #     whereQ=whereQ+" AND dataElement != 'm15'"
            # if new_data['m16'] and new_data['q16']:
            #     insert_new(new_data['m16'], new_data['q16'],"m16")
            #     whereQ=whereQ+" AND dataElement != 'm16'"
            # if new_data['m17'] and new_data['q17']:
            #     insert_new(new_data['m17'], new_data['q17'],"m17")
            #     whereQ=whereQ+" AND dataElement != 'm17'"
            # if new_data['m18'] and new_data['q18']:
            #     insert_new(new_data['m18'], new_data['q18'],"m18")
            #     whereQ=whereQ+" AND dataElement != 'm18'"
            # if new_data['m19'] and new_data['q19']:
            #     insert_new(new_data['m19'], new_data['q19'],"m19")
            #     whereQ=whereQ+" AND dataElement != 'm19'"
            # if new_data['m20'] and new_data['q20']:
            #     insert_new(new_data['m20'], new_data['q20'],"m20")
            #     whereQ=whereQ+" AND dataElement != 'm20'"
            # if new_data['m21'] and new_data['q21']:
            #     insert_new(new_data['m21'], new_data['q21'],"m21")
            #     whereQ=whereQ+" AND dataElement != 'm21'"
            # if new_data['m22'] and new_data['q22']:
            #     insert_new(new_data['m22'], new_data['q22'],"m22")
            #     whereQ=whereQ+" AND dataElement != 'm22'"
            # if new_data['m23'] and new_data['q23']:
            #     insert_new(new_data['m23'], new_data['q23'],"m23")
            #     whereQ=whereQ+" AND dataElement != 'm23'"
            # if new_data['m24'] and new_data['q24']:
            #     insert_new(new_data['m24'], new_data['q24'],"m24")
            #     whereQ=whereQ+" AND dataElement != 'm24'"
            
            # # delete from stock data where record not equal data
            # deleteQ = "DELETE FROM stock_data "+whereQ
            # print(deleteQ)
            # connect_database.cursor().execute(deleteQ)
            # delete_result = connect_database.cursor().fetchall()
            # print(len(delete_result))
        








        # #GET all medicine with quantity and check on stock data (database)
        # jsonStr1 = json.dumps(the_big_data_newest_list)
        # for NumberOfMRecord in range(len(jsonStr1)):
        #     allMData=the_big_data_newest_list[NumberOfMRecord]
        #     addsql = "SELECT id FROM stock_data WHERE tei = %s AND program = %s AND orgUnit = %s AND dataElement = %s"
        #     addattr = (allMData['tei'],allMData['program'],allMData['orgunit'],allMData['dataElement'])
        #     connect_database.cursor().execute(addsql, addattr)
        #     addresult = connect_database.cursor().fetchall()
        #     if(len(addresult)==0):
        #         #if not exist then insert new record 
        #         insSQL = "INSERT INTO stock_data (tei, program, orgunit, date, dataElement, m, q) VALUES (%s ,%s , %s,%s,	%s,	%s,%s)"
        #         insVal = (allMData['tei'], allMData['program'], allMData['orgunit'], allMData['date'], allMData['dataElement'], allMData['m'], allMData['q'])
        #         connect_database.cursor().execute(insSQL, insVal)
        #         connect_database.commit()
        #         print(connect_database.cursor().rowcount, "record inserted.")
        #     else:
        #         #if exist then update record 
        #         updateSQL = "UPDATE stock_data SET  m=%s, q=%s, edit_date=%s WHERE tei= %s AND program= %s AND orgUnit = %s AND dataElement = %s"
        #         updateVal = (allMData['m'],allMData['q'],allMData['edit_date'],allMData['tei'],allMData['program'],allMData['orgunit'],allMData['dataElement'])
        #         connect_database.cursor().execute(updateSQL, updateVal)
        #         connect_database.commit()
        #         print(connect_database.cursor().rowcount, "record Updated.")
        # #select and store all stock data by medicine and orgunit
        # sumQ = "SELECT orgunit,m,SUM(q) AS q FROM stock_data GROUP BY m,orgunit"
        # connect_database.cursor().execute(sumQ)
        # sumResult = connect_database.cursor().fetchall()
        # mydict = []
        # print(sumResult)
        # for row in sumResult:
        #     mydict.append({"orgunit":row[0],"m":row[1],"q":str(row[2])})
        # stud_json = json.dumps(mydict)
        # print(stud_json)

