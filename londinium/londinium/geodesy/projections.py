""" Interconversion between different coordinate systems. """

import numpy as np
from .coordinates import make_canonical_ll


class TransverseMercator(object):
    """ A Transverse Mercator projection. """

    def __init__(self, lon0, lat0, e0, n0, f0, ellipsoid):
        self.lon0 = lon0 * np.pi/180
        self.lat0 = lat0 * np.pi/180
        self.e0 = e0
        self.n0 = n0
        self.f0 = f0
        self.ell = ellipsoid


    def _m(self, lat):
        """ Intermediate calculation for projections. """
        lat_, lat_plus = lat-self.lat0, lat+self.lat0

        n_pow = [1, self.ell.n, self.ell.n**2, self.ell.n**3]

        return self.ell.b * self.f0 * (
             np.dot([1, 1,  5/4,   5/4], n_pow) * lat_
            -np.dot([0, 3,    3,  21/8], n_pow) * np.sin(  lat_) * np.cos(  lat_plus)
            +np.dot([0, 0, 15/8,  15/8], n_pow) * np.sin(2*lat_) * np.cos(2*lat_plus)
            -np.dot([0, 0,    0, 35/24], n_pow) * np.sin(3*lat_) * np.cos(3*lat_plus)
        )


    def ll_to_en(self, lon_lat):
        """ Project from ellipsoid coordinates to plane easting and northing. """

        lon, lat = make_canonical_ll(lon_lat)
        m = self._m(lat)

        s, c = np.sin(lat), np.cos(lat)
        t2 = (s/c)**2
        nu  = self.ell.a * self.f0 * (1 - self.ell.e2 * s**2)**-0.5
        eta2 = (1 - self.ell.e2 * s**2) / (1 - self.ell.e2) - 1

        e_coeffs = [(nu) * c,
                    (nu/6) * c**3 * (1 - t2 + eta2),
                    (nu/120) * c**5 * (5 - 18*t2 + t2**2 + 14*eta2 - 58*t2*eta2)]

        n_coeffs = [(nu/2) * s * c,
                    (nu/24) * s * c**3 * (5 - t2 + 9*eta2),
                    (nu/720) * s * c**5 * (61 - 58*t2 + t2**2)]

        lon_ = lon - self.lon0
        odd_pow, even_pow = [lon_, lon_**3, lon_**5], [lon_**2, lon_**4, lon_**6]

        e_rel = np.sum(np.multiply(e_coeffs, odd_pow), axis=0)
        n_rel = np.sum(np.multiply(n_coeffs, even_pow), axis=0) + m

        return np.stack((e_rel + self.e0, n_rel + self.n0), axis=1)


    def en_to_ll(self, easting_northing):
        """ Project from plane easting and northing to ellipsoid coordinates. """

        e, n = make_canonical_en(easting_northing)
        n_ = n-self.n0
        lat = self.lat0 + n_ / (self.ell.a * self.f0)
        m = self._m(lat)

        while np.mean(np.abs(n_ - m)) > 10**-5:
            lat = lat + (n_ - m) / (self.ell.a * self.f0)
            m = self._m(lat)

        s, sec = np.sin(lat), 1/np.cos(lat)
        t = s*sec
        nu  = self.ell.a * self.f0 * (1 - self.ell.e2 * s**2)**-0.5
        rho = self.ell.a * self.f0 * (1 - self.ell.e2 * s**2)**-1.5 * (1 - self.ell.e2)
        eta2 = nu/rho - 1

        lon_coeffs = [ sec/(nu),
                      -sec/(6*nu**3) * (nu/rho + 2*t**2),
                       sec/(120*nu**5) * (5 + 28*t**2 + 24*t**4),
                      -sec/(5040*nu**7) * (61 + 662*t**2 + 1320*t**4 + 720*t**6)]

        lat_coeffs = [-t/(2*rho*nu),
                       t/(24*rho*nu**3) * (5 + eta2 + (3 - 9*eta2)*t**2),
                      -t/(720*rho*nu**5) * (61 + 90*t**2 + 45*t**4)]

        e_ = e - self.e0
        odd_pow, even_pow = [e_, e_**3, e_**5, e_**7], [e_**2, e_**4, e_**6]

        lon_rel = np.sum(np.multiply(lon_coeffs, odd_pow), axis=0)
        lat_rel = np.sum(np.multiply(lat_coeffs, even_pow), axis=0)

        return np.stack((lon_rel + self.lon0, lat_rel + self.lat0), axis=1)


class UTM29(TransverseMercator):
    """ Universal Transverse Mercator zone 29. """
    def __init__(self, ellipsoid):
        super().__init__(
            lon0=-9,
            lat0=0,
            e0=500000,
            n0=0,
            f0=0.9996,
            ellipsoid=ellipsoid)


class NationalGrid(TransverseMercator):
    def __init__(self, ellipsoid):
        super().__init__(
            lon0=-2,
            lat0=49,
            e0=400000,
            n0=-100000,
            f0=0.9996012717,
            ellipsoid=ellipsoid
        )
