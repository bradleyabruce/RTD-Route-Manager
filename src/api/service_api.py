from classes.service import Service
from utils import connection

def get_service_for_trip(trip_id):
    service_query = f'''
        SELECT 
           c.service_id,
           c.monday,
           c.tuesday,
           c.wednesday,
           c.thursday,
           c.friday,
           c.saturday,
           c.sunday,
           c.start_date,
           c.end_date
        FROM [CALENDAR] c
        LEFT JOIN [TRIPS] t ON t.service_id = c.service_id
        WHERE t.trip_id = {trip_id}'''
    
    service = connection.query_into_object(service_query, Service)
    return service