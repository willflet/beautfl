""" Containers for storing paths to data files in a canonical way.

File types are stored alongside the string paths, which may be specified by arbitrary folder structure or left as default.
"""

import json
import yaml
import os.path
from collections import namedtuple
from abc import abstractmethod

from .json import DisusedStationsFile, OSIFile
from .geojson import GeoJSONLinesFile, GeoJSONStationsFile


def get_datapaths(tfl_data_basedir, repo_data_basedir,
                  tfl_custom_paths=None, repo_custom_paths=None):
    """ Make data path config objects. """

    tfl_data_paths = TfLDataPaths(tfl_data_basedir, tfl_custom_paths)
    repo_data_paths = RepoDataPaths(repo_data_basedir, repo_custom_paths)

    AllDataPaths = namedtuple('AllDatapaths', ['tfl', 'repo'])
    return AllDataPaths(tfl=tfl_data_paths, repo=repo_data_paths)


class _DataPaths(object):
    """ Base class for storing data paths. """

    def __init__(self, basedir, custom_paths=None):
        """"""

        self._basedir = basedir
        if custom_paths is not None:
            self.set_paths(**custom_paths)
        else:
            self.set_paths()

    @property
    def basedir(self):
        return self._basedir

    @abstractmethod
    def set_paths(self, **kwargs):
        """ Store absolute paths to data specified from basedir and kwargs. """

    def abspath(self, relative_path):
        return os.path.join(self.basedir, relative_path)

    @classmethod
    def from_yaml(cls, basedir, yaml_filename):
        """ Make paths from a config yaml file. """
        with open(yaml_filename, 'r') as f:
            custom_paths = yaml.safe_load(f)
        return cls(basedir, custom_paths=custom_paths)

    @classmethod
    def from_json(cls, basedir, json_filename):
        """ Make paths from a config json file. """
        with open(json_filename, 'r') as f:
            custom_paths = json.load(f)
        return cls(basedir, custom_paths=custom_paths)


class RepoDataPaths(_DataPaths):
    """ Config for reading `data supplied in this repository`__.

    .. _repodata: https://github.com/willflet/tfl-transform/tree/master/londinium/data
    __ repodata_
    """

    StationsPaths = namedtuple('StationsPaths',
        ['tfl', 'nr', 'disused', 'depths']
    )
    NRPaths = namedtuple('NRPaths',
        ['z16', 'all']
    )
    LinesPaths = namedtuple('LinesPaths',
        ['tfl', 'nr']
    )
    AreasPaths = namedtuple('AreasPaths',
        ['london', 'river', 'zones']
    )
    OSIPaths = namedtuple('OSIPaths',
        ['json', 'xlsx']
    )

    def __init__(self, basedir, custom_paths=None):
        """ Build paths for finding data files.

        Custom paths for any or all of the files can be defined through a dict
        using the keywords of :method:`set_paths` as keys.

        Otherwise, default structure should be the following::

            basedir/
            ├── dylanmaryk/
            │   └── disused-stations.json
            ├── oobrien/
            │   ├── 2247.json
            │   ├── nontfl_zonal_stations.json
            │   ├── nr_lines.json
            │   ├── nr_stations.json
            │   ├── osis.json
            │   ├── river_thames_simp.json
            │   ├── tfl_lines.json
            │   ├── tfl_stations.json
            │   └── zones1to6.json
            └── TfL/
                ├── out-of-station-interchanges.xlsx
                └── Station depths.csv

        Args:
            basedir:        Base directory where this data is stored. Can be
                            ``""`` if supplying absolute custom_paths.
            custom_paths:   Dictionary describing where (in basedir) to find
                            each file.
        """

        super().__init__(basedir, custom_paths)


    def set_paths(self,
        disused_stations='dylanmaryk/disused-stations.json',
        greater_london='oobrien/2247.json',
        tfl_stations='oobrien/tfl_stations.json',
        rail_stations_london='oobrien/nontfl_zonal_stations.json',
        rail_stations_all='oobrien/nr_stations.json',
        rail_lines='oobrien/nr_lines.json',
        osis_json='oobrien/osis.json',
        river_thames='oobrien/river_thames_simp.json',
        tfl_lines='oobrien/tfl_lines.json',
        zone_boundaries='oobrien/zones1to6.json',
        osis_xlsx='TfL/out-of-station-interchanges.xlsx',
        station_depths='TfL/Station depths.csv'
    ):
        """ Set path hierarchy for datafiles. """

        self.stations = self.StationsPaths(
            tfl=(self.abspath(tfl_stations), GeoJSONStationsFile),
            nr=self.NRPaths(
                z16=(self.abspath(rail_stations_london), GeoJSONStationsFile),
                all=(self.abspath(rail_stations_all), GeoJSONStationsFile)
            ),
            disused=(self.abspath(disused_stations), DisusedStationsFile),
            depths=(self.abspath(station_depths), None)
        )
        self.lines=self.LinesPaths(
            tfl=(self.abspath(tfl_lines), GeoJSONLinesFile),
            nr=(self.abspath(rail_lines), GeoJSONLinesFile)
        )
        self.areas=self.AreasPaths(
            london=(self.abspath(greater_london), None),
            river=(self.abspath(river_thames), None),
            zones=(self.abspath(zone_boundaries), None)
        )
        self.osis = self.OSIPaths(
            json=(self.abspath(osis_json), OSIFile),
            xlsx=(self.abspath(osis_xlsx), None)
        )


class TfLDataPaths(_DataPaths):
    """ Config for reading TfL Open Data from file. """

    StopsPaths = namedtuple('StopsPaths',
        ['boat', 'bus', 'underground']
    )
    RoutesPaths = namedtuple('RoutesPaths',
        ['bus']
    )
    TimetablesPaths = namedtuple('TimetablesPaths',
        ['boat', 'bus', 'cablecar', 'dlr', 'tram', 'underground']
    )
    PassengersPaths = namedtuple('PassengersPaths',
        ['counts', 'rods', 'oyster']
    )

    def __init__(self, basedir, custom_paths=None):
        """ Build paths for finding TfL data files.

        Custom paths for any or all of the files can be defined through a dict
        using the keywords of :method:`set_paths` as keys.

        Otherwise, default structure should be the following::

            basedir/
            ├── stops/
            │   ├── bus-stops.csv
            │   ├── stations.kml
            │   └── pierlocations-v1.kml
            ├── routes/
            │   └── bus-sequences.csv
            ├── timetables/
            │   ├── boat/
            │   ├── bus/
            │   ├── cablecar/
            │   ├── dlr/
            │   ├── tram/
            │   └── underground/
            └── passengers/
                ├── counts/
                ├── RODS_2017/
                └── Nov09JnyExport.csv

        Args:
            basedir:        Base directory where this data is stored. Can be
                            ``""`` if supplying absolute custom_paths.
            custom_paths:   Dictionary describing where (in basedir) to find
                            each file.
        """

        super().__init__(basedir, custom_paths)


    def set_paths(self,
        stops_boat='stops/pierlocations-v1.kml',
        stops_bus='stops/bus-stops.csv',
        stops_underground='stops/stations.kml',
        routes_bus='routes/bus-sequences.csv',
        tt_boat='timetables/boat/tfl_3*.xml',
        tt_bus='timetables/bus/tfl_*.xml',
        tt_cablecar='timetables/cablecar/tfl_71-*.xml',
        tt_dlr='timetables/dlr/tfl_25-*.xml',
        tt_tram='timetables/tram/tfl_63-*.xml',
        tt_underground='timetables/underground/tfl_1-*.xml',
        pax_counts='passengers/counts/',
        pax_rods='passengers/RODS_2017/',
        pax_oyster='passengers/Nov09JnyExport.csv'
    ):
        """ Set path hierarchy for datafiles. """

        self.stops = self.StopsPaths(
            boat=self.abspath(stops_boat),
            bus=self.abspath(stops_bus),
            underground=self.abspath(stops_underground)
        )
        self.routes = self.RoutesPaths(
            bus=self.abspath(routes_bus)
        )
        self.timetables = self.TimetablesPaths(
            boat=self.abspath(tt_boat),
            bus=self.abspath(tt_bus),
            cablecar=self.abspath(tt_cablecar),
            dlr=self.abspath(tt_dlr),
            tram=self.abspath(tt_tram),
            underground=self.abspath(tt_underground)
        )
        self.passengers = self.PassengersPaths(
            counts=self.abspath(pax_counts),
            rods=self.abspath(pax_rods),
            oyster=self.abspath(pax_oyster)
        )
