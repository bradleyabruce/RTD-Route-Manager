from dataclasses import dataclass
from typing import Optional
import utils.connection as connection

@dataclass
class Route:
     route_id: str
     agency_id: Optional[str] = None
     route_short_name: Optional[str] = None
     route_long_name: Optional[str] = None
     route_desc: Optional[str] = None
     route_type: Optional[int] = None
     route_url: Optional[str] = None
     route_color: Optional[str] = None
     route_text_color: Optional[str] = None

     # init class to create object from dictionary.
     def __init__(self, dictionary):
          for key, value in dictionary.items():
               setattr(self, key, value)
