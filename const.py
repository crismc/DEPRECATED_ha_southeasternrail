"""Constants for the ha-southeastern integration."""

DOMAIN = "southeastern"

DEFAULT_NAME = "Southeastern Rail"
DEFAULT_ICON = "mdi:train"

NATIONAL_RAIL_URL = "https://lite.realtime.nationalrail.co.uk/OpenLDBWS/ldb9.asmx"
SOAP_ACTION_URL = (
    "http://thalesgroup.com/RTTI/2015-05-14/ldb/GetNextDeparturesWithDetails"
)

CONF_API_KEY = "api_key"
CONF_ARRIVAL = "arrival"
CONF_DESTINATIONS = "destination"
CONF_TIME_OFFSET = "time_offset"
CONF_TIME_WINDOW = "time_window"
