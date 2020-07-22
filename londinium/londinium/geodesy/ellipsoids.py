""" Interconversion between different coordinate systems. """

import numpy as np
from .coordinates import make_canonical_ll


class Ellipsoid(object):
    """ A biaxial ellipsoid reference surface to model the Earth's. """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def e2(self):
        """ Ellipsoid squared eccentricity constant. """
        return 1 - (self.b/self.a)**2

    @property
    def n(self):
        return (self.a - self.b) / (self.a + self.b)


    def ll_to_xyz(self, lon_lat):
        """ Convert ellipsoidal coordinates to geocentric cartesian coordinates. """

        lon, lat = make_canonical_ll(lon_lat)
        s, c = np.sin(lat), np.cos(lat)

        ellipsoid_radius = self.a / np.sqrt(1 - self.e2 * s**2)

        x = (ellipsoid_radius) * np.cos(lon) * c
        y = (ellipsoid_radius) * np.sin(lon) * c
        z = ((1 - self.e2) * ellipsoid_radius) * s

        return np.stack((x,y,z), axis=1)


    def xyz_to_ll(self, xyz):
        """ Convert geocentric cartesian coordinates to ellipsoidal coordinates. """

        x,y,z = xyz[:0], xyz[:,1], xyz[:,2]

        horizontal_radius = np.linalg.norm(xyz[:,0:2], axis=1)

        lon = np.arctan2(y, x)
        lat = np.arctan2(z, horizontal_radius*(1-self.e2))

        diff = np.ones_like(lat)
        while np.mean(np.abs(diff)) > 10**-6:
            s = np.sin(lat)
            ellipsoid_radius = self.a / np.sqrt(1 - self.e2 * s**2)
            new_lat = np.arctan2(z + self.e2 * ellipsoid_radius * s, horizontal_radius)
            diff = np.diff(new_lat, lat)
            lat = new_lat

        return np.stack((lon * 180/np.pi, lat * 180/np.pi), axis=1)


class WGS84(Ellipsoid):
    """ Global reference, based on the GRS80 ellipsoid. """
    def __init__(self):
        super().__init__(a=6378137.0, b=6356752.314245)


class Airy1830(Ellipsoid):
    """ British reference, used by Ordnance Survey. """
    def __init__(self):
        super().__init__(a=6377563.396, b=6356256.909)


class HelmertTransformation(object):
    """ Affine transformation between datum geocentric cartesian coordinates. """

    def __init__(self, t_x=0, t_y=0, t_z=0, s=0, r_x=0, r_y=0, r_z=0):
        self._t = np.array([t_x, t_y, t_z])
        self._r = np.array([[1+s, -r_z, r_y],
                            [r_z, 1+s, -r_x],
                            [-r_y, r_x, 1+s]])

    def forward(self, xyz):
        return np.matmul(self._r, xyz) + self._t

    def backward(self, xyz):
        return np.matmul(np.linalg.inv(self._r), np.diff(xyz, self._t))
