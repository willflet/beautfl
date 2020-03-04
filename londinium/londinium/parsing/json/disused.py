""" For reading json file containing disused stations. """

import json
from ...util.cached_property import cached_property


class DisusedStationsFile(object):
    """"""

    def __init__(self, path):
        self.path = path


    @cached_property
    def root(self):
        return self._get_root()

    def _get_root(self):
        with open(self.path, 'r') as f:
            root = json.load(f)
        return root


    @property
    def stations(self):
        return self._get_stations()

    def _get_stations(self):
        for e in self.root:
            yield self.DisusedStation(e)


    class DisusedStation(object):
        """"""

        def __init__(self, e):
            self.e = e

        @property
        def id(self):
            return 'DISUSED_{}'.format(self.name)

        @property
        def name(self):
            return self.e['station']

        @property
        def lines(self):
            return self.e['line'].split(', ')

        @property
        def location(self):
            lat, long = self.e['coordinates'].split()
            return (float(lat), float(long))

        @property
        def date_closed(self):
            return self.e['closed']

        @property
        def type_of_closure(self):
            return self.e['type_of_closure']

        @property
        def details(self):
            return self.e['details']

        @property
        def current_condition(self):
            return self.e['current_condition']

        @property
        def image_url(self):
            return self.e['image']
