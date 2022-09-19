from datetime import datetime, timedelta
import xmltodict
import re

def checkKey(dic, key):
    if key in dic.keys():
        return True
    else:
        return False

class ApiData:
    def __init__(self):
        self.raw_result = ""
        self._last_update = None
        self._api_xml = []
        self._station_name = ""
        self._refresh_interval = 2

    def populate(self, xml_data):
        self.raw_result = xml_data
        self._last_update = datetime.now()

    def is_data_stale(self):
        if len(self.raw_result) > 0:
            now = datetime.now()
            staleTime = self._last_update + timedelta(minutes=self._refresh_interval)

            if staleTime < now:
                return False

        return True

    def get_data(self):
        if self.raw_result:
            if not self._api_xml:
                formatted = re.sub(r"lt[0-9]\:", "", self.raw_result)
                data = xmltodict.parse(formatted)
                if data and checkKey(data, "soap:Envelope"):
                    self._api_xml = data["soap:Envelope"]["soap:Body"]["GetNextDeparturesWithDetailsResponse"]["DeparturesBoard"]
            return self._api_xml

    def is_empty(self):
        return len(self._api_xml) == 0

    def get_destination_data(self, station):
        data = self.get_data()
        if data and checkKey(data, "departures"):
            destinations = data["departures"]["destination"]
            if destinations:
                for destination in destinations:
                    if destination["@crs"] == station:
                        service = destination["service"]
                        if checkKey(service, "serviceType"):
                            return service

    def get_service_details(self,crx):
        data = self.get_destination_data(crx)
        del data["subsequentCallingPoints"]
        return data

    def get_calling_points(self,crx):
        data = self.get_destination_data(crx)
        return data["subsequentCallingPoints"]["callingPointList"]["callingPoint"]

    def get_station_name(self):
        if not self._station_name:
            data = self.get_data()
            if data:
                name = data["locationName"]
                if name:
                    self._station_name = name
            
        return self._station_name

    def get_destination_name(self, crx):
        data = self.get_destination_data(crx)
        if data:
            if checkKey(data, "destination"):
                return data["destination"]["location"]["locationName"]

    def message(self):
        data = self.get_data()
        if checkKey(data, "nrccMessages"):
            messages = data["nrccMessages"]
            if checkKey(messages, "message"):
                return re.sub(r"this station", self.get_station_name() + ' station', messages["message"])
                

    def get_last_update(self):
        return self._last_update