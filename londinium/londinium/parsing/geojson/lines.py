""" For reading geojson files containing lines. """

import geojson
from collections import defaultdict
from ...util.cached_property import cached_property


class GeoJSONLinesFile(object):
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
    def links(self):
        return self._get_links()

    def _get_links(self):
        for feature in self.root.features:
            yield self._Link(feature)

    @property
    def lines(self):
        return self._get_lines()

    def _get_lines(self):
        lines = defaultdict(list)
        for link in self.links:
            for link_line in link.link_lines:
                lines[link_line.name].append(link)

        for line_name, links in lines.items():
            yield self._Line(line_name, links)


    class _Link(object):
        """"""

        def __init__(self, e):
            self.e = e

        @property
        def id(self):
            return self.e.properties['id']

        @property
        def link_lines(self):
            return self._get_link_lines()

        def _get_link_lines(self):
            for line in self.e.properties['lines']:
                yield self._LinkLine(line)

        @property
        def geometry(self):
            return self.e.geometry.coordinates

        class _LinkLine(object):
            """"""

            def __init__(self, e):
                self.e = e

            @property
            def name(self):
                return self.e['name']

            @property
            def endpoints(self):
                ids = []
                ids.append(self.e['start_sid'])
                ids.append(self.e['end_sid'])
                if 'otend_sid' in self.e:
                    ids.append(self.e['otend_sid'])
                if 'ot2end_sid' in self.e:
                    ids.append(self.e['ot2end_sid'])
                return ids


    class _Line(object):
        """"""

        def __init__(self, name, links):
            self._name = name
            self._links = links

        @property
        def name(self):
            return self._name

        @property
        def links(self):
            return self._links

        @property
        def sections(self):
            return self._get_sections()

        def _get_sections(self):
            sections = defaultdict(list)
            for link in self.links:
                sections[link.id[:-1]].append(link)

            for section_name, links in sections.items():
                if len(links) == 1:
                    yield self._LineSection(links[0].id, links, self)
                else:
                    yield self._LineSection(section_name, links, self)

        class _LineSection(object):
            """"""

            def __init__(self, name, links, line):
                self._name = name
                self._links = links
                self._line = line

            @property
            def name(self):
                return self._name

            @property
            def links(self):
                return self._links

            @property
            def line(self):
                return self._line
