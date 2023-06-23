# Define store and update data from event to local database
import json
from ..data import check, insert_new
from config import stageForPrescribedMedications
import mysql.connector


def store_data(newest_data, database_connection, cursor):
    """
    This function retrieves all new data and inserts or updates a local database with grouped data by organization and medication.

    Parameters:
    - newest_data: A list of new data to be processed.
    - database_connection: The connection object for the database.
    - cursor: The cursor object for executing SQL queries.

    Returns:
    - dictionary_data_json: A JSON string representing the grouped data by organization and medication.
    """
    
    the_big_data_newest_list = []
    for number_of_new_data in range(len(newest_data)):
        new_data = newest_data[number_of_new_data]
        if(new_data['stage'] == stageForPrescribedMedications):
            # check if this row of data exist or not
            first_sql = "SELECT id FROM row_data_prescribed WHERE event_id=%s AND tei_id = %s AND program_id = %s AND stage_id = %s AND orgunit_id = %s"
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
                first_insert_sql = "INSERT INTO row_data_prescribed (event_id, tei_id, program_id, stage_id, orgunit_id, register_date, medication_code_01, medication_quantity_01, medication_code_02, medication_quantity_02, medication_code_03, medication_quantity_03, medication_code_04, medication_quantity_04, medication_code_05, medication_quantity_05, medication_code_06, medication_quantity_06, medication_code_07, medication_quantity_07, medication_code_08, medication_quantity_08, medication_code_09, medication_quantity_09, medication_code_10, medication_quantity_10, medication_code_11, medication_quantity_11, last_update_date) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
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
                fist_update_sql = "UPDATE row_data_prescribed SET medication_code_01=%s,medication_quantity_01=%s,medication_code_02=%s,medication_quantity_02=%s,medication_code_03=%s,medication_quantity_03=%s,medication_code_04=%s,medication_quantity_04=%s,medication_code_05=%s,medication_quantity_05=%s,medication_code_06=%s,medication_quantity_06=%s,medication_code_07=%s,medication_quantity_07=%s,medication_code_08=%s,medication_quantity_08=%s,medication_code_09=%s,medication_quantity_09=%s,medication_code_10=%s,medication_quantity_10=%s,medication_code_11=%s,medication_quantity_11=%s,last_update_date=%s WHERE event_id=%s AND tei_id= %s AND program_id= %s AND stage_id= %s AND orgunit_id = %s"
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

    # GET all medicine with quantity and check on stock data (database)
    for NumberOfMRecord in range(len(the_big_data_newest_list)):
        all_medication_data = the_big_data_newest_list[NumberOfMRecord]
        select_stock_query = "SELECT id FROM stock_data WHERE event_id = %s AND tei_id = %s AND program_id = %s AND stage_id = %s AND orgunit_id = %s AND data_element_name = %s"
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
            insert_stock_query = "INSERT INTO stock_data (event_id,tei_id, program_id,stage_id, orgunit_id, register_date, data_element_name, medication_code, medication_quantity) VALUES (%s ,%s , %s,%s,	%s,	%s,%s,%s,%s)"
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
            updateSQL = "UPDATE stock_data SET medication_code=%s, medication_quantity=%s, edit_date=%s WHERE event_id = %s AND tei_id= %s AND program_id= %s AND stage_id= %s AND orgunit_id = %s AND data_element_name = %s"
            updateVal = (all_medication_data['m'], all_medication_data['q'], all_medication_data['edit_date'], all_medication_data['event_id'], all_medication_data['tei'],
                         all_medication_data['program'], all_medication_data['stage'], all_medication_data['orgunit'], all_medication_data['dataElement'])
            try:
                cursor.execute(updateSQL, updateVal)
            except mysql.connector.Error as error:
                # Handle the exception
                print(f"Error occurred: {error}")
            database_connection.commit()
    # Select and store all stock data by medicine and orgunit
    sum_query = "SELECT orgunit_id,medication_code,SUM(medication_quantity) AS medication_total_quantity FROM stock_data GROUP BY medication_code,orgunit_id"
    try:
        cursor.execute(sum_query)
    except mysql.connector.Error as error:
        # Handle the exception
        print(f"Error occurred: {error}")
    sum_result = cursor.fetchall()
    my_dictionary_data = []
    for row_in_sum in sum_result:
        my_dictionary_data.append(
            {"orgunit_id": row_in_sum[0], "medication_code": row_in_sum[1], "medication_total_quantity": str(row_in_sum[2])})
    dictionary_data_json = json.dumps(my_dictionary_data)
    return dictionary_data_json
