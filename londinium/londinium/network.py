""" Representations of transport networks. """

import numpy as np


WAYS = ('rail', 'road', 'river', 'cable')


class Mode(object):
    """ Collection of lines operating the same way. """

    def __init__(self, name, way='rail'):
        self._name = name
        self._way = way

        self._lines = dict()

    @property
    def name(self):
        return self._name

    @property
    def way(self):
        return self._way

    @way.setter
    def way(self, value):
        self.check_way(value)
        self._way = way.lower()

    @staticmethod
    def check_way(way):
        if way.lower() not in WAYS:
            raise ValueError('way must be one of {}.'.format(WAYS))

    @property
    def lines(self):
        return self._lines

    def add_line(self, line):
        self._lines.update({line.name:line})


class Line(object):
    """ Distinct service within a mode. May contain some pattern variations. """

    def __init__(self, name):
        self._name = name

        self._stops = dict()
        self._links = list()

    @property
    def name(self):
        return self._name

    @property
    def colour(self):
        return self._colour

    @property
    def links(self):
        return self._stops
        # return set(*section.links for section in self.sections)

    def add_link(self, link):
        self._links.append(link)

    @property
    def stops(self):
        return self._stops
        # return set(*section.stops for section in self.sections)

    def add_stop(self, stop):
        self._stops.update({stop.id:stop})


class Section(object):
    """ Contiguous branch of a line, bounded by Stop at junction or terminus. """

    def __init__(self, name, stop_1, stop_2, links):
        self._name = name
        self.endpoints = (stop_1, stop_2)
        self._links = links

    @property
    def name(self):
        return self._name

    @property
    def links(self):
        return self._links

    @property
    def stops(self):
        return self._stops
        # return set(*link.stops for link in self.links)


class Stop(object):
    """ Point for passengers to alight or depart. """

    def __init__(self, id, name, location, elevation=None, disused=False):
        self.id = id
        self.name = name
        self._location = location
        self.elevation = elevation

        self.disused = disused

    @property
    def location(self):
        return self._location


class Link(object):
    """ Topological connection between two Stops on a Line. """

    def __init__(self, stop_1, stop_2, distance=None, geometry=None, time=None):
        self._stop_1 = stop_1
        self._stop_2 = stop_2
        self._distance = distance
        self._geometry = geometry
        self._time = time

    @property
    def line(self):
        return self._line

    @property
    def stop_1(self):
        return self._stop_1

    @property
    def stop_2(self):
        return self._stop_2

    @property
    def geometry(self):
        return self._geometry or [self.stop_1.location, self.stop_2.location]

    @property
    def distance(self):
        if self._distance is not None:
            return self._distance
        else:
            return sum(np.linalg.norm(v) for v in np.diff(self.geometry, axis=0))


class Interchange(object):
    """ Ties several Stops into an internal or external walking interchange. """

    def __init__(self, stops, name=None):
        self._stops = stops

    @property
    def stops(self):
        return self._stops

    def distance(self, stop_1, stop_2):
        return np.linalg.norm(np.subtract(stop_1.location, stop_2.location))


class Pattern(object):
    """ Service pattern, decribing how the line is operated. """

    def __init__(self):
        pass
