from g4s.utils.static_utils import StaticUtils
from datetime import datetime
from typing import Optional


class TimeZone:
    def __init__(self, input_dict: dict[str, any]) -> None:
        self.country_code: str = input_dict.get("CountryCode")
        self.time_zone_id: int = input_dict.get("TimeZoneId")
        self.olson_name: str = input_dict.get("OlsonName")
        self.is_enabled: bool = input_dict.get("IsEnabled")
        self.name: str = input_dict.get("Name")

    def date_time_as_utc(self, string_date: Optional[str]) -> Optional[datetime]:
        if string_date is None:
            return None
        date_time = StaticUtils.parse_date(string_date)
        date_time = StaticUtils.replace_tz(date_time, self.olson_name)
        date_time = StaticUtils.datetime_to_utc(date_time)
        return date_time
