from dataclasses import dataclass
from classes.stop import Stop
from classes.trip import Trip
from datetime import datetime, time
from typing import Optional

@dataclass
class Stop_Time:
    trip_id: str
    stop_id: str
    arrival_time: time
    departure_time: time
    stop_sequence: int
    stop_headsign: Optional[str]
    pickup_type: str
    drop_off_type: str
    shape_dist_traveled: Optional[str]
    timepoint: str
    stop: Stop
    trip: Trip

    # init class to create object from dictionary.
    def __init__(self, dictionary):
            for key, value in dictionary.items():

                # Convert arrival_time and departure_time to time object.
                if key.lower() == 'arrival_time' or key.lower() == 'departure_time':           
                    value = datetime.strptime(value, '%H:%M:%S').time()
                
                setattr(self, key, value)