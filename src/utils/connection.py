import duckdb
from pathlib import Path


CURRENT_DATA_FOLDER = 'data_20260927_20270102'
DATA_FILE_PLACEHOLDERS = [
     {"placeholder": "[AGENCY]", "data_file": "agency.csv"},
     {"placeholder": "[CALENDAR_DATES]", "data_file": "calendar_dates.csv"},
     {"placeholder": "[CALENDAR]", "data_file": "calendar.csv"},
     {"placeholder": "[FEED_INFO]", "data_file": "feed_info.csv"},
     {"placeholder": "[ROUTES]", "data_file": "routes.csv"},
     {"placeholder": "[SHAPES]", "data_file": "shapes.csv"},
     {"placeholder": "[STOP_TIMES]", "data_file": "stop_times.csv"},
     {"placeholder": "[STOPS]", "data_file": "stops.csv"},
     {"placeholder": "[TRIPS]", "data_file": "trips.csv"},
]


#**************************************
# get_data_directory
#    - Returns absolute path as string of current data directory.
#**************************************
def get_data_directory():
     current_directory = Path(__file__).resolve().parent
     data_folder = str(current_directory.parent / "data" / CURRENT_DATA_FOLDER)
     return data_folder


#**************************************
# replace_sql_placeholders_with_data_file_names
#    - Replace table placeholder names with actual data file name
#**************************************
def replace_sql_placeholders_with_data_file_names(sql):     
     
     for data_file_placeholder in DATA_FILE_PLACEHOLDERS:
          sql = sql.replace(
               data_file_placeholder["placeholder"], 
               "read_csv_auto('" + get_data_directory() + "/" + data_file_placeholder["data_file"] + "')"
          )
     return sql


#**************************************
# query()
#    - Replaces keywords in given 'sql' statement to make it compatible with duckdb.
#    - Uses that sql statement to return a dataframe object.
#**************************************
def query(sql):
     try:
          sql = replace_sql_placeholders_with_data_file_names(sql)
     
          conn = duckdb.connect()
          result = conn.sql(sql).df()
          conn.close()
     
          return result

     except duckdb.BinderException as bind_exception:
          print(f'''Connection.Query() - An error occured: {bind_exception}''')


#**************************************
# query_into_object()
#    - Returns query() function's result parsed into a given object.
#**************************************
def query_into_object(sql_query, datatype):
     query_result = query(sql_query)

     if query_result is None:
          return None

     query_results_count = len(query_result)
     
     # Return None if query returned no results.
     if query_results_count == 0:
          return None

     # Return single object if query returned 1 result.
     elif query_results_count == 1:
          query_result_dictionary = query_result.iloc[0].to_dict()
          return datatype(query_result_dictionary)
     
     # Return array of objects if query returned multiple results.
     # Not yet implemented.
     else:
          objectArray = []

          # Loop through every result, convert it to the requested type, and add it to our array to return.
          for result_index in range(query_results_count):
               result_dictionary = query_result.iloc[result_index].to_dict()
               result_object = datatype(result_dictionary)
               objectArray.append(result_object)

          return objectArray