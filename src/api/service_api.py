from classes.service import Service
from utils import connection

#***********************************
# get_service_by_service_id
#   - Queries calendar.csv for matching service_id record.
#   - Returns Service object.
#***********************************
def get_service_by_service_id(service_id):
    service_query = f'''
        SELECT
            service_id,
            monday,
            tuesday,
            wednesday,
            thursday,
            friday,
            saturday,
            sunday,
            start_date,
            end_date
        FROM [CALENDAR]
        WHERE service_id = '{service_id}'
        LIMIT 1'''

    service = connection.query_into_object(service_query, Service)
    return service

#***********************************
# get_service_for_trip
#   - Queries calendar.csv and trips.csv for trip record's service record.
#   - Returns Service object.
#***********************************
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

#***********************************
# get_days_for_service
#   - Returns array of day names that a given service record is active for.
#   - Returns array of strings.
#***********************************
def get_days_for_service(service_id):
    active_days = []
    service = get_service_by_service_id(service_id)

    if service is not None:
        if service.sunday:
            active_days.append('Sunday')
        if service.monday:
            active_days.append('Monday')
        if service.tuesday:
            active_days.append('Tuesday')
        if service.wednesday:
            active_days.append('Wednesday')
        if service.thursday:
            active_days.append('Thursday')
        if service.friday:
            active_days.append('Friday')
        if service.saturday:
            active_days.append('Saturday')

    return active_days