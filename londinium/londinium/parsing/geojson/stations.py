""" For reading geojson files containing stations. """

import geojson
from collections import defaultdict
from ...util.cached_property import cached_property


class GeoJSONStationsFile(object):
    """"""

    def __init__(self, path):
        self.path = path

    @cached_property
    def root(self):
        return self._get_root()

    def _get_root(self):
        with open(self.path, 'r') as f:
            root = geojson.load(f)
        return root

    @property
    def stations(self):
        return self._get_stations()

    def _get_stations(self):
        for feature in self.root.features:
            yield self._Station(feature)


    class _Station(object):
        """"""

        def __init__(self, e):
            self.e = e

        @property
        def id(self):
            return self.e.properties['id']

        @property
        def alt_id(self):
            if 'alt_id' in self.e.properties:
                return self.e.properties['alt_id']

        @property
        def nlc_id(self):
            if 'nlc_id' in self.e.properties:
                return self.e.properties['nlc_id']

        @property
        def other_mode_ids(self):
            ids = []
            if 'altmodeid' in self.e.properties:
                ids.append(self.e.properties['altmodeid'])
            if 'altmodeid2' in self.e.properties:
                ids.append(self.e.properties['altmodeid2'])
            return ids

        @property
        def name(self):
            return self.e.properties['name']

        @property
        def lines(self):
            return list(line['name'] for line in self.e.properties['lines'])

        @property
        def cartography(self):
            c = self.e.properties['cartography']
            name = c['display_name'] if 'display_name' in c else self.name
            x = c.labelX if 'labelX' in c else 0
            y = c.labelY if 'labelY' in c else 0
            return {name: (x,y)}

        @property
        def zone(self):
            return self.e.properties['zone']

        @property
        def location(self):
            return self.e.geometry.coordinates
