# Define store and update data from event to local database
import json
from ..data import check, insert_new
from config import stageForFrequentlyMedications, stageForPrescribedMedications
import mysql.connector

# This function get all new data and insert or update local database with return new object of grouping data by org and medication


def store_data(newest_data, database_connection, cursor):
    the_big_data_newest_list = []
    for number_of_new_data in range(len(newest_data)):
        new_data = newest_data[number_of_new_data]
        if(new_data['stage'] == stageForPrescribedMedications):
            # check if this row of data exist or not
            first_sql = "SELECT id FROM row_data_prescribed WHERE event_id=%s AND tei = %s AND program = %s AND stage = %s AND orgUnit = %s"
            first_adr = (new_data['event_id'], new_data['tei'],
                         new_data['program'], new_data['stage'], new_data['orgunit'])
            try:
                cursor.execute(first_sql, first_adr)
            except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")

            first_result = cursor.fetchall()
            if(len(first_result) == 0):
                # if not exist insert new row to database
                first_insert_sql = "INSERT INTO row_data_prescribed (event_id,tei,program,stage,orgUnit,date,m1,q1,m2,q2,m3,q3,m4,q4,m5,q5,m6,q6,m7,q7,m8,q8,m9,q9,m10,q10,m11,q11,last_update) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
                first_insert_value = (new_data['event_id'], new_data['tei'], new_data['program'], new_data['stage'], new_data['orgunit'], new_data['date'], new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']), new_data['m5'], check(
                    new_data['q5']), new_data['m6'], check(new_data['q6']), new_data['m7'], check(new_data['q7']), new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']), new_data['m10'], check(new_data['q10']), new_data['m11'], check(new_data['q11']), new_data['last_update'])
                try:
                    cursor.execute(first_insert_sql, first_insert_value)
                    database_connection.commit()
                except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")
            else:
                # if exist update the row
                fist_update_sql = "UPDATE row_data_prescribed SET m1=%s,q1=%s,m2=%s,q2=%s,m3=%s,q3=%s,m4=%s,q4=%s,m5=%s,q5=%s,m6=%s,q6=%s,m7=%s,q7=%s,m8=%s,q8=%s,m9=%s,q9=%s,m10=%s,q10=%s,m11=%s,q11=%s,last_update=%s WHERE event_id=%s AND tei= %s AND program= %s AND stage= %s AND orgUnit = %s"
                fist_update_value = (new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']), new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']), new_data['m7'], check(
                    new_data['q7']), new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']), new_data['m10'], check(new_data['q10']), new_data['m11'], check(new_data['q11']), new_data['last_update'], new_data['event_id'], new_data['tei'], new_data['program'], new_data['stage'], new_data['orgunit'])

                try:
                    cursor.execute(fist_update_sql, fist_update_value)
                    database_connection.commit()
                except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")
            where_query = "WHERE event_id= '" + new_data['event_id']+"' AND tei = '" + new_data['tei']+"' AND program = '" + \
                new_data['program']+"' AND stage = '" + new_data['stage'] + \
                "' AND orgunit='" + new_data['orgunit']+"'"

            if new_data['m1'] and new_data['q1']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m1'], new_data['q1'], "m1", new_data))
                where_query = where_query+" AND dataElement != 'm1'"
            if new_data['m2'] and new_data['q2']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m2'], new_data['q2'], "m2", new_data))
                where_query = where_query+" AND dataElement != 'm2'"
            if new_data['m3'] and new_data['q3']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m3'], new_data['q3'], "m3", new_data))
                where_query = where_query+" AND dataElement != 'm3'"
            if new_data['m4'] and new_data['q4']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m4'], new_data['q4'], "m4", new_data))
                where_query = where_query+" AND dataElement != 'm4'"
            if new_data['m5'] and new_data['q5']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m5'], new_data['q5'], "m5", new_data))
                where_query = where_query+" AND dataElement != 'm5'"
            if new_data['m6'] and new_data['q6']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m6'], new_data['q6'], "m6", new_data))
                where_query = where_query+" AND dataElement != 'm6'"
            if new_data['m7'] and new_data['q7']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m7'], new_data['q7'], "m7", new_data))
                where_query = where_query+" AND dataElement != 'm7'"
            if new_data['m8'] and new_data['q8']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m8'], new_data['q8'], "m8", new_data))
                where_query = where_query+" AND dataElement != 'm8'"
            if new_data['m9'] and new_data['q9']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m9'], new_data['q9'], "m9", new_data))
                where_query = where_query+" AND dataElement != 'm9'"
            if new_data['m10'] and new_data['q10']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m10'], new_data['q10'], "m10", new_data))
                where_query = where_query+" AND dataElement != 'm10'"
            if new_data['m11'] and new_data['q11']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m11'], new_data['q11'], "m11", new_data))
                where_query = where_query+" AND dataElement != 'm11'"

            # delete from stock data where record not equal data
            delete_query_first = "DELETE FROM stock_data "+where_query
            try:
                cursor.execute(delete_query_first)
            except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")
            delete_result_first = cursor.fetchall()

        if(new_data['stage'] == stageForFrequentlyMedications):
            second_sql = "SELECT id FROM row_data_frequently WHERE event_id = %s AND tei = %s AND program = %s AND stage = %s AND orgUnit = %s"
            second_adr = (new_data['event_id'], new_data['tei'],
                          new_data['program'], new_data['stage'], new_data['orgunit'])
            try:
                cursor.execute(second_sql, second_adr)
                second_result = cursor.fetchall()
            except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")
            if(len(second_result) == 0):
                # if not exist insert new row to database
                second_insert_sql = "INSERT INTO row_data_frequently (event_id,tei,program,stage,orgUnit,date,m1,q1,m2,q2,m3,q3,m4,q4,m5,q5,m6,q6,m7,q7,m8,q8,m9,q9,m10,q10,m11,q11,m12,q12,m13,q13,m14,q14,m15,q15,m16,q16,m17,q17,m18,q18,m19,q19,m20,q20,m21,q21,m22,q22,m23,q23,m24,q24,m25,q25,m26,q26,m27,q27,m28,q28,m29,q29,m30,q30,m31,q31,m32,q32,m33,q33,m34,q34,m35,q35,m36,q36,m37,q37,m38,q38,m39,q39,m40,q40,m41,q41,m42,q42,m43,q43,m44,q44,last_update) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                
                second_insert_value = (new_data['event_id'], new_data['tei'], new_data['program'], new_data['stage'], new_data['orgunit'], new_data['date'], new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']), new_data['m5'], check(new_data['q5']), new_data['m6'], check(
                    new_data['q6']), new_data['m7'], check(new_data['q7']), new_data['m8'], check(new_data['q8']), new_data['m9'], check(new_data['q9']), new_data['m10'], check(new_data['q10']), new_data['m11'], check(new_data['q11']), new_data['m12'], check(new_data['q12']), new_data['m13'], check(new_data['q13']), new_data['m14'], check(new_data['q14']), new_data['m15'],
                     check(new_data['q15']), new_data['m16'], check(new_data['q16']), new_data['m17'], check(new_data['q17']), new_data['m18'], check(new_data['q18']), new_data['m19'], check(new_data['q19']), new_data['m20'], check(new_data['q20']), new_data['m21'], check(new_data['q21']), new_data['m22'], check(new_data['q22']), new_data['m23'], check(new_data['q23']),
                      new_data['m24'], check(new_data['q24']), new_data['m25'], check(new_data['q25']), new_data['m26'], check(new_data['q26']), new_data['m27'], check(new_data['q27']), new_data['m28'], check(new_data['q28']), new_data['m29'], check(new_data['q29']), new_data['m30'], check(new_data['q30']), new_data['m31'], check(new_data['q31']), new_data['m32'], check(new_data['q32']),
                       new_data['m33'], check(new_data['q33']), new_data['m34'], check(new_data['q34']), new_data['m35'], check(new_data['q35']), new_data['m36'], check(new_data['q36']), new_data['m37'], check(new_data['q37']), new_data['m38'], check(new_data['q38']), new_data['m39'], check(new_data['q39']), new_data['m40'], check(new_data['q40']), new_data['m41'], check(new_data['q41']),
                        new_data['m42'], check(new_data['q42']), new_data['m43'], check(new_data['q43']), new_data['m44'], check(new_data['q44']), new_data['last_update'])

                try:
                    cursor.execute(second_insert_sql, second_insert_value)
                    database_connection.commit()
                except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")
            else:
                # if exist update the row
                second_update_sql = "UPDATE row_data_frequently SET m1=%s,q1=%s,m2=%s,q2=%s,m3=%s,q3=%s,m4=%s,q4=%s,m5=%s,q5=%s,m6=%s,q6=%s,m7=%s,q7=%s,m8=%s,q8=%s,m9=%s,q9=%s,m10=%s,q10=%s,m11=%s,q11=%s,m12=%s,q12=%s,m13=%s,q13=%s,m14=%s,q14=%s,m15=%s,q15=%s,m16=%s,q16=%s,m17=%s,q17=%s,m18=%s,q18=%s,m19=%s,q19=%s,m20=%s,q20=%s,m21=%s,q21=%s,m22=%s,q22=%s,m23=%s,q23=%s,m24=%s,q24=%s,m25=%s,q25=%s,m26=%s,q26=%s,m27=%s,q27=%s,m28=%s,q28=%s,m29=%s,q29=%s,m30=%s,q30=%s,m31=%s,q31=%s,m32=%s,q32=%s,m33=%s,q33=%s,m34=%s,q34=%s,m35=%s,q35=%s,m36=%s,q36=%s,m37=%s,q37=%s,m38=%s,q38=%s,m39=%s,q39=%s,m40=%s,q40=%s,m41=%s,q41=%s,m42=%s,q42=%s,m43=%s,q43=%s,m44=%s,q44=%s, last_update=%s WHERE event_id= %s AND tei= %s AND program= %s AND stage= %s AND orgUnit = %s"
                second_update_val = (new_data['m1'], check(new_data['q1']), new_data['m2'], check(new_data['q2']), new_data['m3'], check(new_data['q3']), new_data['m4'], check(new_data['q4']), new_data['m5'], check(new_data['q5']), new_data['m6'], check(new_data['q6']), new_data['m7'], check(new_data['q7']), new_data['m8'], check(new_data['q8']), new_data['m9'], check(
                    new_data['q9']), new_data['m10'], check(new_data['q10']), new_data['m11'], check(new_data['q11']), new_data['m12'], check(new_data['q12']), new_data['m13'], check(new_data['q13']), new_data['m14'], check(new_data['q14']),
                     new_data['m15'], check(new_data['q15']), new_data['m16'], check(new_data['q16']), new_data['m17'], check(new_data['q17']), new_data['m18'], check(new_data['q18']), new_data['m19'], check(new_data['q19']), new_data['m20'], check(new_data['q20']),
                      new_data['m21'], check(new_data['q21']),new_data['m22'], check(new_data['q22']), new_data['m23'], check(new_data['q23']), new_data['m24'], check(new_data['q24']), new_data['m25'], check(new_data['q25']), new_data['m26'], check(new_data['q26']),
                       new_data['m27'], check(new_data['q27']),new_data['m28'], check(new_data['q28']), new_data['m29'], check(new_data['q29']), new_data['m30'], check(new_data['q30']), new_data['m31'], check(new_data['q31']), new_data['m32'], check(new_data['q32']),
                        new_data['m33'], check(new_data['q33']),new_data['m34'], check(new_data['q34']), new_data['m35'], check(new_data['q35']), new_data['m36'], check(new_data['q36']), new_data['m37'], check(new_data['q37']), new_data['m38'], check(new_data['q38']), 
                        new_data['m39'], check(new_data['q39']),new_data['m40'], check(new_data['q40']), new_data['m41'], check(new_data['q41']), new_data['m42'], check(new_data['q42']), new_data['m43'], check(new_data['q43']), new_data['m44'], check(new_data['q44']),
                     new_data['last_update'], new_data['event_id'], new_data['tei'], new_data['program'], new_data['stage'], new_data['orgunit'])
                try:
                    cursor.execute(second_update_sql, second_update_val)
                    database_connection.commit()
                except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")
            where_query2 = "WHERE event_id= '" + new_data['event_id'] + "' AND tei= '" + new_data['tei']+"' AND program = '" + \
                new_data['program']+"' AND stage = '" + new_data['stage'] + \
                "' AND orgunit='" + new_data['orgunit']+"'"

            if new_data['m1'] and new_data['q1']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m1'], new_data['q1'], "m1", new_data))
                where_query2 = where_query2+" AND dataElement != 'm1'"
            if new_data['m2'] and new_data['q2']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m2'], new_data['q2'], "m2", new_data))
                where_query2 = where_query2+" AND dataElement != 'm2'"
            if new_data['m3'] and new_data['q3']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m3'], new_data['q3'], "m3", new_data))
                where_query2 = where_query2+" AND dataElement != 'm3'"
            if new_data['m4'] and new_data['q4']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m4'], new_data['q4'], "m4", new_data))
                where_query2 = where_query2+" AND dataElement != 'm4'"
            if new_data['m5'] and new_data['q5']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m5'], new_data['q5'], "m5", new_data))
                where_query2 = where_query2+" AND dataElement != 'm5'"
            if new_data['m6'] and new_data['q6']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m6'], new_data['q6'], "m6", new_data))
                where_query2 = where_query2+" AND dataElement != 'm6'"
            if new_data['m7'] and new_data['q7']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m7'], new_data['q7'], "m7", new_data))
                where_query2 = where_query2+" AND dataElement != 'm7'"
            if new_data['m8'] and new_data['q8']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m8'], new_data['q8'], "m8", new_data))
                where_query2 = where_query2+" AND dataElement != 'm8'"
            if new_data['m9'] and new_data['q9']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m9'], new_data['q9'], "m9", new_data))
                where_query2 = where_query2+" AND dataElement != 'm9'"
            if new_data['m10'] and new_data['q10']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m10'], new_data['q10'], "m10", new_data))
                where_query2 = where_query2+" AND dataElement != 'm10'"
            if new_data['m11'] and new_data['q11']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m11'], new_data['q11'], "m11", new_data))
                where_query2 = where_query2+" AND dataElement != 'm11'"
            if new_data['m12'] and new_data['q12']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m12'], new_data['q12'], "m12", new_data))
                where_query2 = where_query2+" AND dataElement != 'm12'"
            if new_data['m13'] and new_data['q13']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m13'], new_data['q13'], "m13", new_data))
                where_query2 = where_query2+" AND dataElement != 'm13'"
            if new_data['m14'] and new_data['q14']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m14'], new_data['q14'], "m14", new_data))
                where_query2 = where_query2+" AND dataElement != 'm14'"
            if new_data['m15'] and new_data['q15']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m15'], new_data['q15'], "m15", new_data))
                where_query2 = where_query2+" AND dataElement != 'm15'"
            if new_data['m16'] and new_data['q16']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m16'], new_data['q16'], "m16", new_data))
                where_query2 = where_query2+" AND dataElement != 'm16'"
            if new_data['m17'] and new_data['q17']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m17'], new_data['q17'], "m17", new_data))
                where_query2 = where_query2+" AND dataElement != 'm17'"
            if new_data['m18'] and new_data['q18']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m18'], new_data['q18'], "m18", new_data))
                where_query2 = where_query2+" AND dataElement != 'm18'"
            if new_data['m19'] and new_data['q19']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m19'], new_data['q19'], "m19", new_data))
                where_query2 = where_query2+" AND dataElement != 'm19'"
            if new_data['m20'] and new_data['q20']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m20'], new_data['q20'], "m20", new_data))
                where_query2 = where_query2+" AND dataElement != 'm20'"
            if new_data['m21'] and new_data['q21']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m21'], new_data['q21'], "m21", new_data))
                where_query2 = where_query2+" AND dataElement != 'm21'"
            if new_data['m22'] and new_data['q22']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m22'], new_data['q22'], "m22", new_data))
                where_query2 = where_query2+" AND dataElement != 'm22'"
            if new_data['m23'] and new_data['q23']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m23'], new_data['q23'], "m23", new_data))
                where_query2 = where_query2+" AND dataElement != 'm23'"
            if new_data['m24'] and new_data['q24']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m24'], new_data['q24'], "m24", new_data))
                where_query2 = where_query2+" AND dataElement != 'm24'"
            if new_data['m25'] and new_data['q25']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m25'], new_data['q25'], "m25", new_data))
                where_query2 = where_query2+" AND dataElement != 'm25'"
            if new_data['m26'] and new_data['q25']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m26'], new_data['q25'], "m26", new_data))
                where_query2 = where_query2+" AND dataElement != 'm26'"
            if new_data['m27'] and new_data['q27']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m27'], new_data['q27'], "m27", new_data))
                where_query2 = where_query2+" AND dataElement != 'm27'"
            if new_data['m28'] and new_data['q28']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m28'], new_data['q28'], "m28", new_data))
                where_query2 = where_query2+" AND dataElement != 'm28'"
            if new_data['m29'] and new_data['q29']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m29'], new_data['q29'], "m29", new_data))
                where_query2 = where_query2+" AND dataElement != 'm29'"
            if new_data['m30'] and new_data['q30']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m30'], new_data['q30'], "m30", new_data))
                where_query2 = where_query2+" AND dataElement != 'm30'"
            if new_data['m31'] and new_data['q31']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m31'], new_data['q31'], "m31", new_data))
                where_query2 = where_query2+" AND dataElement != 'm31'"
            if new_data['m32'] and new_data['q32']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m32'], new_data['q32'], "m32", new_data))
                where_query2 = where_query2+" AND dataElement != 'm32'"
            if new_data['m33'] and new_data['q33']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m33'], new_data['q33'], "m33", new_data))
                where_query2 = where_query2+" AND dataElement != 'm33'"
            if new_data['m34'] and new_data['q34']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m34'], new_data['q34'], "m34", new_data))
                where_query2 = where_query2+" AND dataElement != 'm34'"
            if new_data['m35'] and new_data['q35']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m35'], new_data['q35'], "m35", new_data))
                where_query2 = where_query2+" AND dataElement != 'm35'"
            if new_data['m36'] and new_data['q36']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m36'], new_data['q36'], "m36", new_data))
                where_query2 = where_query2+" AND dataElement != 'm36'"
            if new_data['m37'] and new_data['q37']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m37'], new_data['q37'], "m37", new_data))
                where_query2 = where_query2+" AND dataElement != 'm37'"
            if new_data['m38'] and new_data['q38']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m38'], new_data['q38'], "m38", new_data))
                where_query2 = where_query2+" AND dataElement != 'm38'"
            if new_data['m39'] and new_data['q39']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m39'], new_data['q39'], "m39", new_data))
                where_query2 = where_query2+" AND dataElement != 'm39'"
            if new_data['m40'] and new_data['q40']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m40'], new_data['q40'], "m40", new_data))
                where_query2 = where_query2+" AND dataElement != 'm40'"
            if new_data['m41'] and new_data['q41']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m41'], new_data['q41'], "m41", new_data))
                where_query2 = where_query2+" AND dataElement != 'm41'"
            if new_data['m42'] and new_data['q42']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m42'], new_data['q42'], "m42", new_data))
                where_query2 = where_query2+" AND dataElement != 'm42'"
            if new_data['m43'] and new_data['q43']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m43'], new_data['q43'], "m43", new_data))
                where_query2 = where_query2+" AND dataElement != 'm43'"
            if new_data['m44'] and new_data['q44']:
                the_big_data_newest_list.append(insert_new(
                    new_data['m44'], new_data['q44'], "m44", new_data))
                where_query2 = where_query2+" AND dataElement != 'm44'"

            # delete from stock data where record not equal data
            delete_query_second = "DELETE FROM stock_data "+where_query2
            try:
                cursor.execute(delete_query_second)
            except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")
            delete_result = cursor.fetchall()

    # GET all medicine with quantity and check on stock data (database)
    for NumberOfMRecord in range(len(the_big_data_newest_list)):
        all_medication_data = the_big_data_newest_list[NumberOfMRecord]
        select_stock_query = "SELECT id FROM stock_data WHERE event_id = %s AND tei = %s AND program = %s AND stage = %s AND orgUnit = %s AND dataElement = %s"
        select_stock_value = (all_medication_data['event_id'], all_medication_data['tei'], all_medication_data['program'],
                              all_medication_data['stage'], all_medication_data['orgunit'], all_medication_data['dataElement'])
        try:    
            cursor.execute(select_stock_query, select_stock_value)
        except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")
        select_stock_result = cursor.fetchall()
        if(len(select_stock_result) == 0):
            # if not exist then insert new record
            insert_stock_query = "INSERT INTO stock_data (event_id,tei, program,stage, orgunit, date, dataElement, m, q) VALUES (%s ,%s , %s,%s,	%s,	%s,%s,%s,%s)"
            insert_stock_value = (all_medication_data['event_id'], all_medication_data['tei'], all_medication_data['program'], all_medication_data['stage'],
                                  all_medication_data['orgunit'], all_medication_data['date'], all_medication_data['dataElement'], all_medication_data['m'], all_medication_data['q'])

            try:
                cursor.execute(insert_stock_query, insert_stock_value)
                database_connection.commit()
            except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")
        else:
            # If exist then update record
            updateSQL = "UPDATE stock_data SET m=%s, q=%s, edit_date=%s WHERE event_id = %s AND tei= %s AND program= %s AND stage= %s AND orgUnit = %s AND dataElement = %s"
            updateVal = (all_medication_data['m'], all_medication_data['q'], all_medication_data['edit_date'], all_medication_data['event_id'], all_medication_data['tei'],
                         all_medication_data['program'], all_medication_data['stage'], all_medication_data['orgunit'], all_medication_data['dataElement'])
            try:
                cursor.execute(updateSQL, updateVal)
            except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")
            database_connection.commit()
    # Select and store all stock data by medicine and orgunit
    sum_query = "SELECT orgunit,m,SUM(q) AS q FROM stock_data GROUP BY m,orgunit"
    try:
        cursor.execute(sum_query)
    except mysql.connector.Error as error:
                    # Handle the exception
                    print(f"Error occurred: {error}")
    sum_result = cursor.fetchall()
    my_dictionary_data = []
    for row_in_sum in sum_result:
        my_dictionary_data.append(
            {"orgunit": row_in_sum[0], "m": row_in_sum[1], "q": str(row_in_sum[2])})
    dictionary_data_json = json.dumps(my_dictionary_data)
    return dictionary_data_json
