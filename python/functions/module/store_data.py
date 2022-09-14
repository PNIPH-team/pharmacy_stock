import json
from ..connect_database import connect_database
from ..data import check,insert_new


def store_data(newest_data):
    #if array not empty
    # if not len(newest_data) == 0:
        jsonStr = json.dumps(newest_data)
        #write array data to RowData File
        # writefile(todayDateTime + "/RowData_" +
        #         today_date + ".json", json.loads(jsonStr))
        the_big_data_newest_list = []
        for numberOfNewData in range(len(newest_data)):
            newData=newest_data[numberOfNewData]
            #check if this row of data exist or not
            sql = "SELECT id FROM RowData WHERE tei = %s AND program = %s AND orgUnit = %s"
            adr = (newData['tei'],newData['program'],newData['orgunit'])
            connect_database.cursor().execute(sql, adr)
            my_result = connect_database.cursor().fetchall()
            if(len(my_result)==0):
                #if not exist insert new row to database
                sql = "INSERT INTO RowData (tei,program,orgUnit,date,	m,	q,	m1,	q1,	m2,	q2,	m3,	q3,	m4,	q4,	m5,	q5,	m6,	q6,	m7,	q7,	m8,	q8,	m9,	q9,	m10,	q10,	m11,	q11,	m12,	q12,	m13,	q13,	m14,	q14,	m15,	q15,	m16,	q16,	m17,	q17,	m18,	q18,	m19,	q19,	m20,	q20,	m21,	q21,	m22,	q22,	m23,	q23,	m24,	q24,last_update) VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s)"
                val = (newData['tei'],newData['program'],newData['orgunit'],newData['date'],newData['m'], check(newData['q']), newData['m1'], check(newData['q1']), newData['m2'], check(newData['q2']), newData['m3'], check(newData['q3']), newData['m4'], check(newData['q4']) ,newData['m5'], check(newData['q5']), newData['m6'], check(newData['q6']) ,newData['m7'], check(newData['q7']) ,newData['m8'], check(newData['q8']), newData['m9'], check(newData['q9']) ,newData['m10'], check(newData['q10']),newData['m11'], check(newData['q11']), newData['m12'], check(newData['q12']), newData['m13'], check(newData['q13']), newData['m14'], check(newData['q14']), newData['m15'], check(newData['q15']), newData['m16'], check(newData['q16']), newData['m17'], check(newData['q17']), newData['m18'], check(newData['q18']), newData['m19'], check(newData['q19']), newData['m20'], check(newData['q20']), newData['m21'], check(newData['q21']), newData['m22'], check(newData['q22']), newData['m23'], check(newData['q23']), newData['m24'], check(newData['q24']),newData['last_update'])
                connect_database.cursor().execute(sql, val)
                connect_database.commit()
                print(connect_database.cursor().rowcount, "record inserted.")
            else:
                #if exist update the row
                sql = "UPDATE RowData SET m=%s,q=%s,m1=%s,q1=%s,m2=%s,q2=%s,m3=%s,q3=%s,m4=%s,q4=%s,m5=%s,q5=%s,m6=%s,q6=%s,m7=%s,q7=%s,m8=%s,q8=%s,m9=%s,q9=%s,m10=%s,q10=%s,m11=%s,q11=%s,m12=%s,q12=%s,m13=%s,q13=%s,m14=%s,q14=%s,m15=%s,q15=%s,m16=%s,q16=%s,m17=%s,q17=%s,m18=%s,q18=%s,m19=%s,q19=%s,m20=%s,q20=%s,m21=%s,q21=%s,m22=%s,q22=%s,m23=%s,q23=%s,m24=%s,q24=%s , last_update=%s WHERE tei= %s AND program= %s AND orgUnit = %s"
                val = (newData['m'], check(newData['q']), newData['m1'], check(newData['q1']), newData['m2'], check(newData['q2']), newData['m3'], check(newData['q3']), newData['m4'], check(newData['q4']) ,newData['m5'], check(newData['q5']), newData['m6'], check(newData['q6']) ,newData['m7'], check(newData['q7']) ,newData['m8'], check(newData['q8']), newData['m9'], check(newData['q9']) ,newData['m10'], check(newData['q10']),newData['m11'], check(newData['q11']), newData['m12'], check(newData['q12']), newData['m13'], check(newData['q13']), newData['m14'], check(newData['q14']), newData['m15'], check(newData['q15']), newData['m16'], check(newData['q16']), newData['m17'], check(newData['q17']), newData['m18'], check(newData['q18']), newData['m19'], check(newData['q19']), newData['m20'], check(newData['q20']), newData['m21'], check(newData['q21']), newData['m22'], check(newData['q22']), newData['m23'], check(newData['q23']), newData['m24'], check(newData['q24']),newData['last_update'],newData['tei'],newData['program'],newData['orgunit'])
                connect_database.cursor().execute(sql, val)
                connect_database.commit()
                print(connect_database.cursor().rowcount, "record Updated.")
            whereQ='WHERE '+"tei= '"+ newest_data[numberOfNewData]['tei']+"' AND program = '"+ newest_data[numberOfNewData]['program']+"' AND orgunit='"+ newest_data[numberOfNewData]['orgunit']+"'"
            if newest_data[numberOfNewData]['m'] and newest_data[numberOfNewData]['q']:
                insert_new(newest_data[numberOfNewData]['m'], newest_data[numberOfNewData]['q'],"m")
                whereQ=whereQ+" AND dataElement != 'm'"
            if newest_data[numberOfNewData]['m1'] and newest_data[numberOfNewData]['q1']:
                insert_new(newest_data[numberOfNewData]['m1'], newest_data[numberOfNewData]['q1'],"m1")
                whereQ=whereQ+" AND dataElement != 'm1'"
            if newest_data[numberOfNewData]['m2'] and newest_data[numberOfNewData]['q2']:
                insert_new(newest_data[numberOfNewData]['m2'], newest_data[numberOfNewData]['q2'],"m2")
                whereQ=whereQ+" AND dataElement != 'm2'"
            if newest_data[numberOfNewData]['m3'] and newest_data[numberOfNewData]['q3']:
                insert_new(newest_data[numberOfNewData]['m3'], newest_data[numberOfNewData]['q3'],"m3")
                whereQ=whereQ+" AND dataElement != 'm3'"
            if newest_data[numberOfNewData]['m4'] and newest_data[numberOfNewData]['q4']:
                insert_new(newest_data[numberOfNewData]['m4'], newest_data[numberOfNewData]['q4'],"m4")
                whereQ=whereQ+" AND dataElement != 'm4'"
            if newest_data[numberOfNewData]['m5'] and newest_data[numberOfNewData]['q5']:
                insert_new(newest_data[numberOfNewData]['m5'], newest_data[numberOfNewData]['q5'],"m5")
                whereQ=whereQ+" AND dataElement != 'm5'"
            if newest_data[numberOfNewData]['m6'] and newest_data[numberOfNewData]['q6']:
                insert_new(newest_data[numberOfNewData]['m6'], newest_data[numberOfNewData]['q6'],"m6")
                whereQ=whereQ+" AND dataElement != 'm6'"
            if newest_data[numberOfNewData]['m7'] and newest_data[numberOfNewData]['q7']:
                insert_new(newest_data[numberOfNewData]['m7'], newest_data[numberOfNewData]['q7'],"m7")
                whereQ=whereQ+" AND dataElement != 'm7'"
            if newest_data[numberOfNewData]['m8'] and newest_data[numberOfNewData]['q8']:
                insert_new(newest_data[numberOfNewData]['m8'], newest_data[numberOfNewData]['q8'],"m8")
                whereQ=whereQ+" AND dataElement != 'm8'"
            if newest_data[numberOfNewData]['m9'] and newest_data[numberOfNewData]['q9']:
                insert_new(newest_data[numberOfNewData]['m9'], newest_data[numberOfNewData]['q9'],"m9")
                whereQ=whereQ+" AND dataElement != 'm9'"
            if newest_data[numberOfNewData]['m10'] and newest_data[numberOfNewData]['q10']:
                insert_new(newest_data[numberOfNewData]['m10'], newest_data[numberOfNewData]['q10'],"m10")
                whereQ=whereQ+" AND dataElement != 'm10'"
            if newest_data[numberOfNewData]['m11'] and newest_data[numberOfNewData]['q11']:
                insert_new(newest_data[numberOfNewData]['m11'], newest_data[numberOfNewData]['q11'],"m11")
                whereQ=whereQ+" AND dataElement != 'm11'"
            if newest_data[numberOfNewData]['m12'] and newest_data[numberOfNewData]['q12']:
                insert_new(newest_data[numberOfNewData]['m12'], newest_data[numberOfNewData]['q12'],"m12")
                whereQ=whereQ+" AND dataElement != 'm12'"
            if newest_data[numberOfNewData]['m13'] and newest_data[numberOfNewData]['q13']:
                insert_new(newest_data[numberOfNewData]['m13'], newest_data[numberOfNewData]['q13'],"m13")
                whereQ=whereQ+" AND dataElement != 'm13'"
            if newest_data[numberOfNewData]['m14'] and newest_data[numberOfNewData]['q14']:
                insert_new(newest_data[numberOfNewData]['m14'], newest_data[numberOfNewData]['q14'],"m14")
                whereQ=whereQ+" AND dataElement != 'm14'"
            if newest_data[numberOfNewData]['m15'] and newest_data[numberOfNewData]['q15']:
                insert_new(newest_data[numberOfNewData]['m15'], newest_data[numberOfNewData]['q15'],"m15")
                whereQ=whereQ+" AND dataElement != 'm15'"
            if newest_data[numberOfNewData]['m16'] and newest_data[numberOfNewData]['q16']:
                insert_new(newest_data[numberOfNewData]['m16'], newest_data[numberOfNewData]['q16'],"m16")
                whereQ=whereQ+" AND dataElement != 'm16'"
            if newest_data[numberOfNewData]['m17'] and newest_data[numberOfNewData]['q17']:
                insert_new(newest_data[numberOfNewData]['m17'], newest_data[numberOfNewData]['q17'],"m17")
                whereQ=whereQ+" AND dataElement != 'm17'"
            if newest_data[numberOfNewData]['m18'] and newest_data[numberOfNewData]['q18']:
                insert_new(newest_data[numberOfNewData]['m18'], newest_data[numberOfNewData]['q18'],"m18")
                whereQ=whereQ+" AND dataElement != 'm18'"
            if newest_data[numberOfNewData]['m19'] and newest_data[numberOfNewData]['q19']:
                insert_new(newest_data[numberOfNewData]['m19'], newest_data[numberOfNewData]['q19'],"m19")
                whereQ=whereQ+" AND dataElement != 'm19'"
            if newest_data[numberOfNewData]['m20'] and newest_data[numberOfNewData]['q20']:
                insert_new(newest_data[numberOfNewData]['m20'], newest_data[numberOfNewData]['q20'],"m20")
                whereQ=whereQ+" AND dataElement != 'm20'"
            if newest_data[numberOfNewData]['m21'] and newest_data[numberOfNewData]['q21']:
                insert_new(newest_data[numberOfNewData]['m21'], newest_data[numberOfNewData]['q21'],"m21")
                whereQ=whereQ+" AND dataElement != 'm21'"
            if newest_data[numberOfNewData]['m22'] and newest_data[numberOfNewData]['q22']:
                insert_new(newest_data[numberOfNewData]['m22'], newest_data[numberOfNewData]['q22'],"m22")
                whereQ=whereQ+" AND dataElement != 'm22'"
            if newest_data[numberOfNewData]['m23'] and newest_data[numberOfNewData]['q23']:
                insert_new(newest_data[numberOfNewData]['m23'], newest_data[numberOfNewData]['q23'],"m23")
                whereQ=whereQ+" AND dataElement != 'm23'"
            if newest_data[numberOfNewData]['m24'] and newest_data[numberOfNewData]['q24']:
                insert_new(newest_data[numberOfNewData]['m24'], newest_data[numberOfNewData]['q24'],"m24")
                whereQ=whereQ+" AND dataElement != 'm24'"
            
            # delete from stock data where record not equal data
            deleteQ = "DELETE FROM stock_data "+whereQ
            print(deleteQ)
            connect_database.cursor().execute(deleteQ)
            delete_result = connect_database.cursor().fetchall()
            print(len(delete_result))
        
        #GET all medicine with quantity and check on stock data (database)
        jsonStr1 = json.dumps(the_big_data_newest_list)
        for NumberOfMRecord in range(len(jsonStr1)):
            allMData=the_big_data_newest_list[NumberOfMRecord]
            addsql = "SELECT id FROM stock_data WHERE tei = %s AND program = %s AND orgUnit = %s AND dataElement = %s"
            addattr = (allMData['tei'],allMData['program'],allMData['orgunit'],allMData['dataElement'])
            connect_database.cursor().execute(addsql, addattr)
            addresult = connect_database.cursor().fetchall()
            if(len(addresult)==0):
                #if not exist then insert new record 
                insSQL = "INSERT INTO stock_data (tei, program, orgunit, date, dataElement, m, q) VALUES (%s ,%s , %s,%s,	%s,	%s,%s)"
                insVal = (allMData['tei'], allMData['program'], allMData['orgunit'], allMData['date'], allMData['dataElement'], allMData['m'], allMData['q'])
                connect_database.cursor().execute(insSQL, insVal)
                connect_database.commit()
                print(connect_database.cursor().rowcount, "record inserted.")
            else:
                #if exist then update record 
                updateSQL = "UPDATE stock_data SET  m=%s, q=%s, edit_date=%s WHERE tei= %s AND program= %s AND orgUnit = %s AND dataElement = %s"
                updateVal = (allMData['m'],allMData['q'],allMData['edit_date'],allMData['tei'],allMData['program'],allMData['orgunit'],allMData['dataElement'])
                connect_database.cursor().execute(updateSQL, updateVal)
                connect_database.commit()
                print(connect_database.cursor().rowcount, "record Updated.")
        #select and store all stock data by medicine and orgunit
        sumQ = "SELECT orgunit,m,SUM(q) AS q FROM stock_data GROUP BY m,orgunit"
        connect_database.cursor().execute(sumQ)
        sumResult = connect_database.cursor().fetchall()
        mydict = []
        print(sumResult)
        for row in sumResult:
            mydict.append({"orgunit":row[0],"m":row[1],"q":str(row[2])})
        stud_json = json.dumps(mydict)
        print(stud_json)
    # else:
    #     print("EmptyData")
        # writefile(todayDateTime + "/JobSummary" +
        #         today_date + ".json", json.dumps([{"0": "EmptyData"}]))
