# Define store and update data from event to local database
import json
from ..data import check,insert_new

# This function get all new data and insert or update local database with return new object of grouping data by org and medication
def store_data(newest_data,database_connection,cursor):
        the_big_data_newest_list = []
        for number_of_new_data in range(len(newest_data)):
            new_data=newest_data[number_of_new_data]
            if(new_data['stage']=="JV6n7FhC7xp"):
                #check if this row of data exist or not
                first_sql = "SELECT id FROM row_data_prescribed WHERE event_id=%s AND tei = %s AND program = %s AND stage = %s AND orgUnit = %s"
                first_adr = (new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'])
                cursor.execute(first_sql, first_adr)
                first_result = cursor.fetchall()
                if(len(first_result)==0):
                    #if not exist insert new row to database
                    first_insert_sql = "INSERT INTO row_data_prescribed (event_id,tei,program,stage,orgUnit,date,m1,q1,m2,q2,m3,q3,m4,q4,m5,q5,m6,q6,m7,q7,m8,q8,m9,q9,m10,q10,m11,q11,last_update) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
                    first_insert_value = (new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'],new_data['date'], new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']),new_data['last_update'])
                    cursor.execute(first_insert_sql, first_insert_value)
                    database_connection.commit()
                else:
                    #if exist update the row
                    fist_update_sql = "UPDATE row_data_prescribed SET m1=%s,q1=%s,m2=%s,q2=%s,m3=%s,q3=%s,m4=%s,q4=%s,m5=%s,q5=%s,m6=%s,q6=%s,m7=%s,q7=%s,m8=%s,q8=%s,m9=%s,q9=%s,m10=%s,q10=%s,m11=%s,q11=%s,last_update=%s WHERE event_id=%s AND tei= %s AND program= %s AND stage= %s AND orgUnit = %s"
                    fist_update_value = (new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']),new_data['last_update'],new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'])
                    cursor.execute(fist_update_sql, fist_update_value)
                    database_connection.commit()
                where_query="WHERE event_id= '"+ new_data['event_id']+"' AND tei = '"+ new_data['tei']+"' AND program = '"+ new_data['program']+"' AND stage = '"+ new_data['stage']+"' AND orgunit='"+ new_data['orgunit']+"'"
      
                if new_data['m1'] and new_data['q1']:
                    the_big_data_newest_list.append(insert_new(new_data['m1'],new_data['q1'],"m1",new_data))
                    where_query=where_query+" AND dataElement != 'm1'"
                if new_data['m2'] and new_data['q2']:
                    the_big_data_newest_list.append(insert_new(new_data['m2'], new_data['q2'],"m2",new_data))
                    where_query=where_query+" AND dataElement != 'm2'"
                if new_data['m3'] and new_data['q3']:
                    the_big_data_newest_list.append(insert_new(new_data['m3'], new_data['q3'],"m3",new_data))
                    where_query=where_query+" AND dataElement != 'm3'"
                if new_data['m4'] and new_data['q4']:
                    the_big_data_newest_list.append(insert_new(new_data['m4'], new_data['q4'],"m4",new_data))
                    where_query=where_query+" AND dataElement != 'm4'"
                if new_data['m5'] and new_data['q5']:
                    the_big_data_newest_list.append(insert_new(new_data['m5'], new_data['q5'],"m5",new_data))
                    where_query=where_query+" AND dataElement != 'm5'"
                if new_data['m6'] and new_data['q6']:
                    the_big_data_newest_list.append(insert_new(new_data['m6'], new_data['q6'],"m6",new_data))
                    where_query=where_query+" AND dataElement != 'm6'"
                if new_data['m7'] and new_data['q7']:
                    the_big_data_newest_list.append(insert_new(new_data['m7'], new_data['q7'],"m7",new_data))
                    where_query=where_query+" AND dataElement != 'm7'"
                if new_data['m8'] and new_data['q8']:
                    the_big_data_newest_list.append(insert_new(new_data['m8'], new_data['q8'],"m8",new_data))
                    where_query=where_query+" AND dataElement != 'm8'"
                if new_data['m9'] and new_data['q9']:
                    the_big_data_newest_list.append(insert_new(new_data['m9'], new_data['q9'],"m9",new_data))
                    where_query=where_query+" AND dataElement != 'm9'"
                if new_data['m10'] and new_data['q10']:
                    the_big_data_newest_list.append(insert_new(new_data['m10'], new_data['q10'],"m10",new_data))
                    where_query=where_query+" AND dataElement != 'm10'"
                if new_data['m11'] and new_data['q11']:
                    the_big_data_newest_list.append(insert_new(new_data['m11'], new_data['q11'],"m11",new_data))
                    where_query=where_query+" AND dataElement != 'm11'"
         
                
                # delete from stock data where record not equal data
                delete_query_first = "DELETE FROM stock_data "+where_query
                cursor.execute(delete_query_first)
                delete_result_first = cursor.fetchall()

            if(new_data['stage']=="tJQ1UCpkCy2"):
                second_sql = "SELECT id FROM row_data_frequently WHERE event_id = %s AND tei = %s AND program = %s AND stage = %s AND orgUnit = %s"
                second_adr = (new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'])
                cursor.execute(second_sql, second_adr)
                second_result = cursor.fetchall()
                if(len(second_result)==0):
                    #if not exist insert new row to database
                    second_insert_sql = "INSERT INTO row_data_frequently (event_id,tei,program,stage,orgUnit,date,m1,q1,m2,q2,m3,q3,m4,q4,m5,q5,m6,q6,m7,q7,m8,q8,m9,q9,m10,q10,m11,q11,m12,q12,m13,q13,m14,q14,last_update) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    second_insert_value = (new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'],new_data['date'], new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']),new_data['m12'], check(new_data['q12']),new_data['m13'], check(new_data['q13']),new_data['m14'], check(new_data['q14']),new_data['last_update'])
                    cursor.execute(second_insert_sql, second_insert_value)
                    database_connection.commit()
                else:
                    #if exist update the row
                    second_update_sql = "UPDATE row_data_frequently SET m1=%s,q1=%s,m2=%s,q2=%s,m3=%s,q3=%s,m4=%s,q4=%s,m5=%s,q5=%s,m6=%s,q6=%s,m7=%s,q7=%s,m8=%s,q8=%s,m9=%s,q9=%s,m10=%s,q10=%s,m11=%s,q11=%s,m12=%s,q12=%s,m13=%s,q13=%s,m14=%s,q14=%s, last_update=%s WHERE event_id= %s AND tei= %s AND program= %s AND stage= %s AND orgUnit = %s"
                    second_update_val = (new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']) ,new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']) ,new_data['m7'], check(new_data['q7']) ,new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']) ,new_data['m10'], check(new_data['q10']),new_data['m11'], check(new_data['q11']),new_data['m12'], check(new_data['q12']),new_data['m13'], check(new_data['q13']),new_data['m14'], check(new_data['q14']),new_data['last_update'],new_data['event_id'],new_data['tei'],new_data['program'],new_data['stage'],new_data['orgunit'])
                    cursor.execute(second_update_sql, second_update_val)
                    database_connection.commit()
                where_query2="WHERE event_id= '"+ new_data['event_id'] + "' AND tei= '"+ new_data['tei']+"' AND program = '"+ new_data['program']+"' AND stage = '"+ new_data['stage']+"' AND orgunit='"+ new_data['orgunit']+"'"
    
                if new_data['m1'] and new_data['q1']:
                    the_big_data_newest_list.append(insert_new(new_data['m1'], new_data['q1'],"m1",new_data))
                    where_query2=where_query2+" AND dataElement != 'm1'"
                if new_data['m2'] and new_data['q2']:
                    the_big_data_newest_list.append(insert_new(new_data['m2'], new_data['q2'],"m2",new_data))
                    where_query2=where_query2+" AND dataElement != 'm2'"
                if new_data['m3'] and new_data['q3']:
                    the_big_data_newest_list.append(insert_new(new_data['m3'], new_data['q3'],"m3",new_data))
                    where_query2=where_query2+" AND dataElement != 'm3'"
                if new_data['m4'] and new_data['q4']:
                    the_big_data_newest_list.append(insert_new(new_data['m4'], new_data['q4'],"m4",new_data))
                    where_query2=where_query2+" AND dataElement != 'm4'"
                if new_data['m5'] and new_data['q5']:
                    the_big_data_newest_list.append(insert_new(new_data['m5'], new_data['q5'],"m5",new_data))
                    where_query2=where_query2+" AND dataElement != 'm5'"
                if new_data['m6'] and new_data['q6']:
                    the_big_data_newest_list.append(insert_new(new_data['m6'], new_data['q6'],"m6",new_data))
                    where_query2=where_query2+" AND dataElement != 'm6'"
                if new_data['m7'] and new_data['q7']:
                    the_big_data_newest_list.append(insert_new(new_data['m7'], new_data['q7'],"m7",new_data))
                    where_query2=where_query2+" AND dataElement != 'm7'"
                if new_data['m8'] and new_data['q8']:
                    the_big_data_newest_list.append(insert_new(new_data['m8'], new_data['q8'],"m8",new_data))
                    where_query2=where_query2+" AND dataElement != 'm8'"
                if new_data['m9'] and new_data['q9']:
                    the_big_data_newest_list.append(insert_new(new_data['m9'], new_data['q9'],"m9",new_data))
                    where_query2=where_query2+" AND dataElement != 'm9'"
                if new_data['m10'] and new_data['q10']:
                    the_big_data_newest_list.append(insert_new(new_data['m10'], new_data['q10'],"m10",new_data))
                    where_query2=where_query2+" AND dataElement != 'm10'"
                if new_data['m11'] and new_data['q11']:
                    the_big_data_newest_list.append(insert_new(new_data['m11'], new_data['q11'],"m11",new_data))
                    where_query2=where_query2+" AND dataElement != 'm11'"
                if new_data['m12'] and new_data['q12']:
                    the_big_data_newest_list.append(insert_new(new_data['m12'], new_data['q12'],"m12",new_data))
                    where_query2=where_query2+" AND dataElement != 'm12'"
                if new_data['m13'] and new_data['q13']:
                    the_big_data_newest_list.append(insert_new(new_data['m13'], new_data['q13'],"m13",new_data))
                    where_query2=where_query2+" AND dataElement != 'm13'"
                if new_data['m14'] and new_data['q14']:
                    the_big_data_newest_list.append(insert_new(new_data['m14'], new_data['q14'],"m14",new_data))
                    where_query2=where_query2+" AND dataElement != 'm14'"
        
                
                # delete from stock data where record not equal data
                delete_query_second = "DELETE FROM stock_data "+where_query2
                cursor.execute(delete_query_second)
                delete_result = cursor.fetchall()


        #GET all medicine with quantity and check on stock data (database)
        for NumberOfMRecord in range(len(the_big_data_newest_list)):
            all_medication_data =  the_big_data_newest_list[NumberOfMRecord]
            select_stock_query = "SELECT id FROM stock_data WHERE event_id = %s AND tei = %s AND program = %s AND stage = %s AND orgUnit = %s AND dataElement = %s"
            select_stock_value = (all_medication_data['event_id'],all_medication_data['tei'],all_medication_data['program'],all_medication_data['stage'],all_medication_data['orgunit'],all_medication_data['dataElement'])
            cursor.execute(select_stock_query, select_stock_value)
            select_stock_result = cursor.fetchall()
            if(len(select_stock_result)==0):
                #if not exist then insert new record 
                insert_stock_query = "INSERT INTO stock_data (event_id,tei, program,stage, orgunit, date, dataElement, m, q) VALUES (%s ,%s , %s,%s,	%s,	%s,%s,%s,%s)"
                insert_stock_value = (all_medication_data['event_id'],all_medication_data['tei'], all_medication_data['program'],all_medication_data['stage'], all_medication_data['orgunit'], all_medication_data['date'], all_medication_data['dataElement'], all_medication_data['m'], all_medication_data['q'])
                cursor.execute(insert_stock_query, insert_stock_value)
                database_connection.commit()
            else:
                # If exist then update record 
                updateSQL = "UPDATE stock_data SET m=%s, q=%s, edit_date=%s WHERE event_id = %s AND tei= %s AND program= %s AND stage= %s AND orgUnit = %s AND dataElement = %s"
                updateVal = (all_medication_data['m'],all_medication_data['q'],all_medication_data['edit_date'],all_medication_data['event_id'],all_medication_data['tei'],all_medication_data['program'],all_medication_data['stage'],all_medication_data['orgunit'],all_medication_data['dataElement'])
                cursor.execute(updateSQL, updateVal)
                database_connection.commit()
        # Select and store all stock data by medicine and orgunit
        sum_query = "SELECT orgunit,m,SUM(q) AS q FROM stock_data GROUP BY m,orgunit"
        cursor.execute(sum_query)
        sum_result = cursor.fetchall()
        my_dictionary_data = []
        for row_in_sum in sum_result:
            my_dictionary_data.append({"orgunit":row_in_sum[0],"m":row_in_sum[1],"q":str(row_in_sum[2])})
        dictionary_data_json = json.dumps(my_dictionary_data)
        return dictionary_data_json

