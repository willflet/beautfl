""" Utilities for manipulating coordinates. """

import numpy as np


def make_canonical_ll(lon_lat):
    """ Get into standard form, as 2D array in radians. """

    ll = np.reshape(lon_lat, (-1, 2))
    lon = ll[:, 0] * np.pi/180
    lat = ll[:, 1] * np.pi/180

    return lon, lat


def make_canonical_en(easting_northing):
    """ Get into standard form, as 2D array. """

    en = np.reshape(easting_northing, (-1, 2))
    easting = en[:, 0]
    northing = en[:, 1]
