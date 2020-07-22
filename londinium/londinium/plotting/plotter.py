""" Plotter for transit maps. """

import numpy as np
import matplotlib.pyplot as plt

from .styles import line_colour_map, line_plot_order
from ..geodesy.projections import NationalGrid
from .distortions import NoDistortion


class Canvas(object):
    """ Matplotlib canvas on which to draw map. """

    def __init__(self,
                 projection=NationalGrid(),
                 distortion=NoDistortion(),
                 bbox=[[-0.54, 0.28],[51.3, 51.7]],
                 **kwargs):

        self.projection = projection
        self.distortion = distortion
        self.bbox = bbox

        self.make_axes(**kwargs)

    def make_axes(self, **kwargs):
        self.f = plt.figure(**kwargs)
        self.ax = plt.Axes(self.f, [0,0,1,1])
        self.f.add_axes(self.ax)
        self.ax.set_aspect('equal')
        self.ax.set_axis_off()


    def plot(self, geometry, check_bbox=False, **kwargs):
        geom = np.reshape(geometry, (-1,2))
        if check_bbox:
            if not self.is_inside_bbox(geom):
                pass
        easting_northing = self.projection.ll_to_en(geom)
        new_geom = self.distortion(easting_northing)

        self.ax.plot(new_geom[:,0], new_geom[:,1], **kwargs)


    def show(self):
        plt.show()


    def is_inside_bbox(self, geometry):
        if (np.amax(geometry[:,0]) < self.bbox[0][0] or
            np.amax(geometry[:,0]) > self.bbox[0][1] or
            np.amax(geometry[:,1]) < self.bbox[1][0] or
            np.amin(geometry[:,1]) > self.bbox[1][1]
            ): return False
        else: return True
