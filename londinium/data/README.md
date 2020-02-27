# data

Small and assorted data files pertaining to London transport.


## dylanmaryk/

Data files prepared by GitHub user [dylanmaryk](https://github.com/dylanmaryk). From [Disused-London-Tube-Stations-Data](https://github.com/dylanmaryk/Disused-London-Tube-Stations-Data). Supplied without license but scraped from open sources.

* `disused-stations.json` -- Copy of https://github.com/dylanmaryk/Disused-London-Tube-Stations-Data/tree/master/data.json


## oobrien/

Data files prepared by GitHub user [oobrien](https://github.com/oobrien). From [vis/tube/data](https://github.com/oobrien/vis/tree/master/tube/data).

### Geographical objects

#### 2D (polygons)
* `2247.json` -- Greater London
* `river_thames_simp.json` -- River Thames
* `zones1to6.json` -- Implied areas of Zones 1-6, inferred from multiple sources.

#### 1D (polylines)
* `nr_lines.json` -- Non-TfL lines (one polyline per trackset)
* `tfl_lines.json` -- TfL lines (one polyline per tunnel pair)

#### 0D (points)
* `nr_stations.json` -- Non-TfL stations
* `tfl_stations.json` -- TfL stations

### Extras
* `nontfl_zonal_stations.json` -- Non-TfL stations within the London zones
* `osis.json` -- Out-of-station interchanges (OSIs)


## TfL/

Miscellaneous data files provided by Transport for London.

* `out-of-station-interchanges.xlsx` -- Excel format list of OSIs. NB see [oobrien/osis.json](#extras) for a more machine-readable format.
* `Station depths.csv` -- From a [FOI request](https://www.whatdotheyknow.com/request/depth_of_tube_lines).


# Additional data used

Larger data sources used in this project (not in this repository) are:

## [TfL Open Data](https://tfl.gov.uk/info-for/open-data-users/our-open-data)

For this project the relevant data were downloaded from the [TfL developer portal] (https://api-portal.tfl.gov.uk/docs), then stored and organized in the folder structure described below.

### passengers/
* `counts/` -- London Underground passenger counts data.
    "Passenger counts collects information about passenger numbers entering and exiting London Underground stations, largely based on the Underground ticketing system gate data."

* `RODS_2017/` -- Rolling Origin & Destination Survey (RODS).
    "The Rolling O&D survey is an ongoing programme to capture information about journeys on the Tube network."
* `Nov09JnyExport.csv` -- Oyster card journey information.
    "This dataset provides a 5% sample of all Oyster card journeys performed in a week during November 2009 on bus, Tube, DLR and London Overground."

### routes/
* `bus-sequences.csv` -- Bus routes.
    "This dataset describes the London Buses standard network information. The network information includes the location of all bus stops in London and the sequence of bus stops that every bus route in London stops at."

### stops/
* `bus-stops.csv` -- Bus stop locations.
    "This dataset contains information about the location and identifiers for each bus stop served by the London bus network."
* `stations.kml` -- Station locations.
    "Our station location feed is a geo-coded KML feed of most London Underground, DLR and London Overground stations." NB see also the [files](#oobrien) prepared by GitHub user [oobrien](https://github.com/oobrien).
* `pierlocations-v1.kml` -- Pier locations
    "Our pier location feed is a geo-coded KML feed of the piers and docks along the River Thames." (NB currently only lists two piers).

### timetables/
Journey Planner timetables

"The Journey Planner timetable feed contains up to date standard timetables for London Underground, bus, DLR and river services." (NB comes in 4 zipped folders for buses and 1 for the rest).

* `boat/` -- XML documents containing Riverboat timetable data
* `bus/` -- XML documents containing London Bus timetable data.
* `cablecar/` -- XML documents containing Emirates Air Line timetable data
* `dlr/` -- XML documents containing Docklands Light Railway timetable data
* `tram/` -- XML documents containing London Trams timetable data
* `underground/` -- XML documents containing London Underground timetable data
