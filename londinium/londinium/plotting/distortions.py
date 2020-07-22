""" Mathematical distortion of geographic objects. """

import numpy as np
from abc import abstractmethod


class Distortion(object):
    """ Some transformation to apply to spatial geometries before plotting."""

    def __init__(self):
        pass

    @abstractmethod
    def __call__(self, geometry):
        return geometry


class NoDistortion(Distortion):
    """ The identity transformation. No effect. """

    def __call__(self, geometry):
        return geometry


class PolarDistortion(Distortion):
    """ A fisheye effect in polar coordinates, distorting radially. """

    def __init__(self,
                 centre=[530500, 181500],
                 radial_transform=lambda x: np.arctan(x/5000)):
        self._centre = centre
        self._radial_transform = radial_transform
        super().__init__()

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
