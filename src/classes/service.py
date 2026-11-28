# Service.py uses information from calendar.csv.
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Service:
    service_id: str
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool
    start_date: datetime
    end_date: datetime

    # init class to create object from dictionary.
    def __init__(self, dictionary):
            for key, value in dictionary.items():

                # Convert 'start_date' and 'end_date' to datetime object.
                if key.lower() == 'start_date' or key.lower() == 'end_date':
                     value = datetime.strptime(str(value), "%Y%m%d")

                # Convert day values to bool objects
                if key.lower() in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                    value = bool(value)
                
                setattr(self, key, value)