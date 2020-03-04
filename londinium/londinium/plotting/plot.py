""" """

import numpy as np
import matplotlib.pyplot as plt

from ..parsing.read import read_repo_data
from .styles import line_colour_map, line_plot_order
from .projections import ll_to_OS, polar_distort


def plot_geometry(ax, distortion):


def plot():
    (disused_stations,
    out_of_station_interchanges,
    tfl_stations,
    nr_all_stations,
    nr_z16_stations,
    tfl_lines,
    nr_links) = read_repo_data()


    tfl_stations_dict = {x.id:x for x in tfl_stations}


    NR = []
    for nr_link in nr_links:
        polyline = np.array(nr_link.geometry)
        if (np.amax(polyline[:,0]) >-0.54 and
            np.amax(polyline[:,0]) < 0.28 and
            np.amax(polyline[:,1]) > 51.3 and
            np.amin(polyline[:,1]) < 51.7
           ):
            NR.append(ll_to_OS(polyline))


    f = plt.figure(figsize=(20,30),dpi=150)
    ax = plt.Axes(f,[0,0,1,1])
    f.add_axes(ax)
    ax.set_aspect('equal')
    ax.set_axis_off()
    for line in tfl_lines:
        for link in line.links:
            geom = polar_distort(ll_to_OS(link.geometry), CENTRE, TRANSFORM)
            ax.plot(geom[:,0], geom[:,1],
                    color=line_colour_map[line.name].hex,
                    linewidth = 1.2,
                    zorder=line_plot_order.index(line.name))

    for station in tfl_stations:
        if len(station.lines) > 1 or station.name in out_of_station_interchanges.stations:
            color = '#FFFFFF'
            size = 4
            edge = '#000000'
            z = 98
        else:
            color = line_colour_map[station.lines[0]].hex
            size = 2
            edge = color
            z = line_plot_order.index(station.lines[0])

        geom = polar_distort(ll_to_os([station.location]), CENTRE, TRANSFORM)
        ax.plot(geom[:,0], geom[:,1],
                mfc=color,
                mec=edge,
                marker='o',
                ms=size,
                zorder=z)


    for station in disused_stations:
        color = '#888888'
        size = 2
        edge = color
        z = 99

        geom = polar_distort(ll_to_OS([station.location]), CENTRE, TRANSFORM)
        ax.plot(geom[:,0], geom[:,1],
                mfc=color,
                mec=edge,
                marker='o',
                ms=size,
                zorder=z)


    for osi in out_of_station_interchanges.osis:
        geom = polar_distort(ll_to_OS([tfl_stations_dict[osi.a].location] + [tfl_stations_dict[osi.b].location]), CENTRE, TRANSFORM)
        ax.plot(geom[:,0], geom[:,1],
                color='#000000',
                lw=3,
                zorder=97)
        ax.plot(geom[:,0],
                geom[:,1],
                color='#FFFFFF',
                lw=1,
                zorder=99)


    for nr_polyline in NR:
        geom = polar_distort(nr_polyline, CENTRE, TRANSFORM)
        ax.plot(geom[:,0], geom[:,1],
                color='#DDDDDD',
                linewidth = 1,
                zorder=line_plot_order.index('National Rail'))
    plt.show()
