import utils.connection as connection
from classes.stop_time import Stop_Time
import api.stop_api as stop_api
import api.trip_api as trip_api

def get_all_stop_times_for_trip_id(trip_id):
    get_all_stop_times_for_trip_query = f'''
        SELECT
            stop_id,
            trip_id,
            arrival_time,
            departure_time,
            stop_sequence,
            stop_headsign,
            pickup_type,
            drop_off_type,
            shape_dist_traveled,
            timepoint
        FROM [STOP_TIMES]
        WHERE trip_id = {trip_id}
        ORDER BY stop_sequence
    '''
    stop_times = connection.query_into_object(get_all_stop_times_for_trip_query, Stop_Time)

    # Populate the Stop and Trip object for each Stop_Time object
    for stop_time in stop_times:
        stop_time.Stop = stop_api.get_stop_by_stop_id(stop_time.stop_id)
        stop_time.Trip = trip_api.get_trip_by_trip_id(stop_time.trip_id)

    return stop_times