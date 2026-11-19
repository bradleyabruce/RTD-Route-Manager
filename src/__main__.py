import api.route_api as route_api

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