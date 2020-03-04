""" Base class for reading a TransXChange file. """

import xml.etree.ElementTree as ET
from collections import defaultdict
from ...util.cached_property import cached_property
from .elements import TXCStopPoint, TXCRouteSection, TXCRoute, TXCService
from ...network import Line, Stop, Link


NS = {'ns': 'http://www.transxchange.org.uk/'}


class TransXChangeFile(object):
    """ Class to store information from a single TransXChange file. """

    def __init__(self, filename):
        self.filename = filename


    @cached_property
    def root(self):
        return self._get_root()

    def _get_root(self):
        print('parsing {}'.format(self.filename))
        return ET.parse(self.filename).getroot()


    @cached_property
    def stop_points(self):
        return self._get_stop_points()

    def _get_stop_points(self):
        elements = self.root.find('ns:StopPoints', namespaces=NS).findall('ns:StopPoint', namespaces=NS)
        stop_points = [TXCStopPoint(e, NS) for e in elements]
        return {x.id:x for x in stop_points}


    @cached_property
    def route_sections(self):
        return self._get_route_sections()

    def _get_route_sections(self):
        elements = self.root.find('ns:RouteSections', namespaces=NS).findall('ns:RouteSection', namespaces=NS)
        route_sections = [TXCRouteSection(e, NS) for e in elements]
        return {x.id:x for x in route_sections}


    @cached_property
    def routes(self):
        return self._get_routes()

    def _get_routes(self):
        elements = self.root.find('ns:Routes', namespaces=NS).findall('ns:Route', namespaces=NS)
        routes = [TXCRoute(e, self.namespace) for e in elements]
        return {x.id:x for x in routes}


    @cached_property
    def service(self):
        return self.get_services()

    def get_services(self):
        elements = self.root.find('ns:Services', namespaces=NS).findall('ns:Service', namespaces=NS)
        if len(elements) > 1:
            raise ValueError('More than one Service present!')
            # services = [Service(e, self.namespace) for e in elements]
            # return {x.id:x for x in services}
        else:
            e = elements[0]
            return TXCService(e, NS)


class TransXChangeLinesFromFiles(object):
    """ Aggregate line data from multiple TfL TransXChange files. """

    def __init__(self, filenames):
        self.filenames = filenames

    @cached_property
    def lines(self):
        return self._agg_lines()

    def _agg_lines(self):
        d = defaultdict(list)
        for filename in self.filenames:
            file = TransXChangeFile(filename)
            d[file.service.line.name].append(file)
        return d


    @cached_property
    def stop_points(self):
        return self._agg_stop_points()

    def _agg_stop_points(self):
        d = defaultdict(dict)
        for linename, files in self.lines.items():
            for file in files:
                for ref, stop_point in file.stop_points.items():
                    if ref in d[linename]:
                        pass # Skip duplicate stops
                    else:
                        d[linename].update({ref:stop_point})
        return d


    @cached_property
    def route_sections(self):
        return self._agg_route_sections()

    def _agg_route_sections(self):
        d = defaultdict(dict)
        for linename, files in self.lines.items():
            for file in files:
                for ref, route_section in file.route_sections.items():
                    from_stop_ref = route_section.route_links[0].fra
                    to_stop_ref = route_section.route_links[-1].to
                    key = (from_stop_ref, to_stop_ref)
                    if key in d[linename]:
                        pass # Skip duplicate route sections
                    else:
                        d[linename].update({key:route_section})
        return d


    @cached_property
    def route_links(self):
        return self._agg_route_links()

    def _agg_route_links(self):
        d = defaultdict(dict)
        for linename, files in self.lines.items():
            for file in files:
                for ref, route_section in file.route_sections.items():
                    for route_link in route_section.route_links:
                        key = (route_link.fra, route_link.to)
                        if key in d[linename]:
                            pass # Skip duplicate route links
                        else:
                            d[linename].update({key:route_link})
        return d


    @cached_property
    def routes(self):
        return self._agg_routes()

    def _agg_routes(self):
        d = defaultdict(list)
        for linename, files in self.lines.items():
            for file in files:
                for ref in file.routes.keys():
                    d[linename].update(ref)
        return d


    @cached_property
    def network(self):
        return self._to_network()

    def _to_network(self):
        """ Read nodes (stops) and edges (links), per line. """

        lines = []

        for linename in self.lines:

            line = Line(
                name=linename
            )

            for ref, stop_point in self.stop_points[linename].items():
                stop = Stop(
                    id=stop_point.id,
                    name=stop_point.name,
                    location=stop_point.location
                )
                line.add_stop(stop)

            for ref, route_link in self.route_links[linename].items():
                link = Link(
                    stop_1 = line.stops[route_link.fra],
                    stop_2 = line.stops[route_link.to],
                    distance = route_link.distance
                )
                line.add_link(link)

            lines.append(line)

        return lines
