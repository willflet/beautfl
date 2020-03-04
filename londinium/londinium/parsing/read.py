""" Read information from all the files available. """

from glob import glob
from .datapaths import get_datapaths
from .transxchange.files import TransXChangeFile, TransXChangeLinesFromFiles
from .json import DisusedStationsFile, OSIFile
from .geojson import GeoJSONLinesFile, GeoJSONStationsFile
from ..network import Mode #, Line, Section, Stop, Link, Interchange, Pattern


TFL_DATA_BASEDIR = '/mnt/c/Users/magic/Datasets/TfL'
REPO_DATA_BASEDIR = './data'

DPATHS = get_datapaths(
    tfl_data_basedir=TFL_DATA_BASEDIR,
    repo_data_basedir=REPO_DATA_BASEDIR
)


def read_repo_data():
    disused_stations = DisusedStationsFile(DPATHS.repo.stations.disused).stations
    out_of_station_interchanges = OSIFile(DPATHS.repo.osis.json)
    tfl_stations = GeoJSONStationsFile(DPATHS.repo.stations.tfl).stations
    nr_all_stations = GeoJSONStationsFile(DPATHS.repo.stations.nr.all).stations
    nr_z16_stations = GeoJSONStationsFile(DPATHS.repo.stations.nr.z16).stations
    tfl_lines = GeoJSONLinesFile(DPATHS.repo.lines.tfl).lines
    nr_links = GeoJSONLinesFile(DPATHS.repo.lines.nr).links

    return (
        disused_stations,
        out_of_station_interchanges,
        tfl_stations,
        nr_all_stations,
        nr_z16_stations,
        tfl_lines,
        nr_links
    )


def read_tfl_data():

    modes = dict()

    for m in ('boat', 'cablecar', 'dlr', 'tram', 'underground'): # 'bus',

        paths = glob(DPATHS.tfl.timetables._asdict()[m])

        mode = modes[m] = Mode(name=m, way='rail')
        txc = TransXChangeLinesFromFiles(paths)

        for line in txc.network: mode.add_line(line)
