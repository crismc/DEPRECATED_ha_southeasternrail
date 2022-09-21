# Southeastern Rail Integration Component by [@crismc](https://github.com/crismc)
A custom Home Assistant component to show next available trains to specific stops through the National Rail Darwin SOAP API.
For better visuals, to be used with the Home Assistant custom card ha-southeastern-rail-card (https://github.com/crismc/ha-southeastern-rail-card)

Creates a sensor for each station/destination, reporting arrival/destination times, and relevant calling stops along the way coupled with any station messages such as delayed or cancelled services.

Based on the HA-LondonTfl component by [@morosanmihail] (https://github.com/morosanmihail/HA-LondonTfL), although the code has taken a side step to incorporate the Darwin SOAP API.

This can be used for any/all stations associated to the National Rail service, and returns service information associated to the GetNextDeparturesWithDetailsRequest.
For information on the SOAP API, visit [Live Departure Boards Web Service (LDBWS / OpenLDBWS)](https://lite.realtime.nationalrail.co.uk/openldbws/)

![Screenshot4](screenshot4.png)

![Screenshot3](screenshot3.png)

## Requirements
As this component intracts with the National Rail Darwin Feed, this requires an API Key to access the LDB Webservice (PV) SOAP API:
https://www.nationalrail.co.uk/100296.aspx

Simply go to the above link and choose [Register Here](http://realtime.nationalrail.co.uk/OpenLDBWSRegistration/Registration) next to LDB Webservice (PV)

## Options

| Name                 | Type    | Requirement  | Description                                                                                       | Default |
| ---------------------| ------- | ------------ | --------------------------------------------------------------------------------------------------|---------|
| api_key              | string  | **Required** | National Rail Darwin Feed API Key                                                                 | `none`  |
| arrival              | string  | **Required** | 3 Letter CRX station code of your local station                                                   | `none`  |
| destination          | string  | **Required** | 3 Letter CRX station code of your target destination station                                      | `none`  |
| time_offset          | string  | **Required** | An offset in minutes against the current time to provide the station board for your local station | `none`  |


## Installing the component from source
This is a new component, and haven't yet got this up onto HACS. Therefore, simpliest way is to manually drop it into your custom_components folder, and restart your Home Assistant configuration.

### Setup
![Screenshot1](screenshot1.png)

You can add integration via the Integrations menu by searching for `ha-southeastern`.
It will ask for an API Key, provide a list of stations to set as your local arrival station, and allow you to set the time offset.
![Screenshot2](screenshot2.png)

Next, it will allow you to add your destination station.
By selecting "Add Another", you can add more destination stations.

Each destination will be created as its own sensor.

Sensor name will change to the name of the local and destination station.

### Alternate setup

Alternatively, you can set it up manually in your `configuration.yaml`.

If configuring this directly within `configuration.yaml`, you will also need to know your stations 3 letter CRX codes. These can be found [here](https://www.nationalrail.co.uk/stations_destinations/48541.aspx)

Demo configuration:

```
sensor:
  - platform: ha-southeastern
    api_key: 1234abcd-1a2b3c-1a2b-9876-123abc456def
    arrival: ABW
    destination: CHX
    time_offset: 20
```

[license-shield]: https://img.shields.io/github/license/custom-cards/boilerplate-card.svg?style=for-the-badge
