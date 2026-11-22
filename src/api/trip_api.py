import utils.connection as connection
from classes.trip import Trip

def get_trip_by_trip_id(trip_id):
    trip_query = f'''
        SELECT 
            trip_id,
            route_id,
            service_id,
            trip_headsign,
            direction_id,
            block_id,
            shape_id
        FROM [TRIPS]
        WHERE trip_id = '{trip_id}'
        LIMIT 1'''
    
    trip = connection.query_into_object(trip_query, Trip)
    return trip

def get_all_trips_for_route_id(route_id):
    all_trips_for_route_query = f'''
        SELECT
            trip_id,
            route_id,
            service_id,
            trip_headsign,
            direction_id,
            block_id,
            shape_id
        FROM [TRIPS]
        WHERE route_id = '{route_id}'
        '''
    trips = connection.query_into_object(all_trips_for_route_query, Trip)
    return trips