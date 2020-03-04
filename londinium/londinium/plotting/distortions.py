""" Mathematical distortion of geographic objects. """

import numpy as np


RADIAL_TRANSFORM = lambda x: np.arctan(x/5000)
CENTRE = [530500, 181500]
DISTORT = lambda x: polar_distort(x, transform=TRANSFORM, centre=CENTRE)


class Location(object)
    def __init__(self):
        pass


class PolarDistortion(object):

    def __init__(self, centre=CENTRE, radial_transform=RADIAL_TRANSFORM):
        self._centre = centre
        self._radial_transform = radial_transform

    def __call__(self, geometry):
        v = np.subtract(geometry, self.centre)
        r = np.linalg.norm(v, axis=1)
        theta = np.arctan2(v[:,1], v[:,0])

        r = self.radial_transform(r)

        new_geometry = np.stack((r*np.cos(theta), r*np.sin(theta)), axis=1)

        return new_geometry

    @property
    def centre(self):
        return np.reshape(self._centre, (1,2))

    def radial_transform(self, r):
        return self._radial_transform(r)
