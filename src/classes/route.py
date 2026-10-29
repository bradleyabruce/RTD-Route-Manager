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

     
     def populate_route(self):
          query = f"""
               SELECT *
               FROM [ROUTES]
               WHERE route_id = '{self.route_id}'
               LIMIT 1"""
          result_array = connection.query(query)
          dataframe_result_object = Route(**result_array.iloc[0].to_dict())

          # Wipes out current attributes and copies the new object's attributes
          self.__dict__.clear()
          self.__dict__.update(dataframe_result_object.__dict__)
