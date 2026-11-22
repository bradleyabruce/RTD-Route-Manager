import utils.connection as connection
from classes.stop import Stop

def get_stop_by_stop_id(stop_id):
    stop_query = f'''
        SELECT 
            stop_id,
            stop_code,
            stop_name,
            stop_desc,
            stop_lat,
            stop_lon,
            zone_id,
            stop_url,
            location_type,
            parent_station,
            stop_timezone,
            wheelchair_boarding,
            platform_code
        FROM [STOPS]
        WHERE stop_id = {stop_id}
        LIMIT 1
        '''
    
    stop = connection.query_into_object(stop_query, Stop)
    return stop