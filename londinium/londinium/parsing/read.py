""" Handle files of known structure into objects for easy data access. """

from glob import glob
from .transxchange.files import TransXChangeFile, TransXChangeLinesFromFiles
from .json import DisusedStationsFile, OSIFile
from .geojson import GeoJSONLinesFile, GeoJSONStationsFile
# from ..network import Mode #, Line, Section, Stop, Link, Interchange, Pattern


def read_repo_data_files(*paths):
    """ Obtain file-parsing objects from data paths"""

    files = []
    for path, parser in paths:
        files.append(parser(path))

    return files


def read_tfl_data():
    """ Work in progress. """

    modes = dict()

    for m in ('boat', 'cablecar', 'dlr', 'tram', 'underground'): # 'bus',

        paths = glob(DPATHS.tfl.timetables._asdict()[m])

        mode = modes[m] = Mode(name=m, way='rail')
        txc = TransXChangeLinesFromFiles(paths)

        for line in txc.network: mode.add_line(line)
