from dataclasses import dataclass
from typing import Optional

@dataclass
class Stop:
    stop_id: str
    stop_code: str
    stop_name: str
    stop_desc: str
    stop_lat: str
    stop_lon: str
    zone_id: str
    stop_url: str
    location_type: str
    parent_station: Optional[str] = None
    stop_timezone: Optional[str] = None
    wheelchair_boarding: Optional[bool] = False
    platform_code: Optional[str] = None

    # init class to create object from dictionary.
    def __init__(self, dictionary):
            for key, value in dictionary.items():
                
                # Convert wheelchair_boarding from string to bool
                if key.lower() == 'wheelchair_boarding':
                    value = bool(value)

                setattr(self, key, value)