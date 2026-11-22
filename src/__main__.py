import api.route_api as route_api
import api.trip_api as trip_api
import api.stop_api as stop_api

route = route_api.get_route_by_route_id(15)
print(route.agency_id)
print(route.route_color)
print(route.route_desc)
print(route.route_id)
print(route.route_long_name)
print(route.route_short_name)
print(route.route_text_color)
print(route.route_type)
print(route.route_url)

trip = trip_api.get_trip_by_trip_id(116031094)
print(trip.trip_id)
print(trip.route_id)
print(trip.block_id)
print(trip.direction_id)
print(trip.trip_headsign)
print(trip.shape_id)

trips = trip_api.get_all_trips_for_route_id(15)
print(len(trips))

stop = stop_api.get_stop_by_stop_id(10007)
print(stop.wheelchair_boarding)