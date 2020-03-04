""" For reading out-of-station-interchanges. """

import json
from ...util.cached_property import cached_property


class OSIFile(object):
    """"""

    def __init__(self, path, format='json'):
        self.path = path
        self.format='json'


    @cached_property
    def root(self):
        return self._get_root()

    def _get_root(self):
        with open(self.path, 'r') as f:
            root = json.load(f)['2020']
        return root

    @property
    def stations(self):
        return self._get_stations()

    def _get_stations(self):
        stations = set()
        for osi in self.osis:
            stations.update({osi.a, osi.b})
        return stations

    @property
    def osis(self):
        return self._get_osis()

    def _get_osis(self):
        for osi in self.root:
            yield self._OSI(osi)


    class _OSI(object):
        """"""

        def __init__(self, e):
            self.e = e

        @property
        def a(self):
            return self.e[0]

        @property
        def b(self):
            return self.e[1]

        @property
        def interchange_type(self):
            return self.e[2]
