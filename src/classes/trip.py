from dataclasses import dataclass
from classes.service import Service

@dataclass
class Trip:
    trip_id: str
    route_id: str
    service_id: str
    trip_headsign: str
    direction_id: str
    block_id: str
    shape_id: str
    service: Service

    # init class to create object from dictionary.
    def __init__(self, dictionary):
            for key, value in dictionary.items():
                setattr(self, key, value)
