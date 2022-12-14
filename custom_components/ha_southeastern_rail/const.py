"""Constants for the ha-southeastern integration."""

DOMAIN = "southeastern-rail"

DEFAULT_NAME = "Southeastern Rail"
DEFAULT_ICON = "mdi:train"
DEFAULT_TIME_OFFSET = 20
DEFAULT_TIME_WINDOW = 120

NATIONAL_RAIL_URL = "https://lite.realtime.nationalrail.co.uk/OpenLDBWS/ldb9.asmx"
SOAP_ACTION_URL = (
    "http://thalesgroup.com/RTTI/2015-05-14/ldb/GetNextDeparturesWithDetails"
)

CONF_API_KEY = "api_key"
CONF_ARRIVAL = "arrival"
CONF_DESTINATIONS = "destination"
CONF_TIME_OFFSET = "time_offset"
CONF_TIME_WINDOW = "time_window"
CONF_REFRESH_SECONDS = 60
