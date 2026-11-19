import utils.connection as connection
from classes.route import Route

def get_route_by_route_id(route_id):
    route_query = f"""
        SELECT 
            route_id,
            agency_id,
            route_short_name,
            route_long_name,
            route_desc,
            route_type,
            route_url,
            route_color,
            route_text_color
        FROM [ROUTES]
        WHERE route_id = '{route_id}'
        LIMIT 1"""
    route = connection.query_into_object(route_query, Route)

    return route