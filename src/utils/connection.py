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
# query
#    - Format sql and then use duckdb to query the data tables.
#**************************************
def query(sql):
     sql = replace_sql_placeholders_with_data_file_names(sql)
     
     conn = duckdb.connect()
     result = conn.sql(sql).df()
     conn.close()
     
     return result