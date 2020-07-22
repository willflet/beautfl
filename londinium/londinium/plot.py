""" Script for plotting a transformed tube map. """

import numpy as np
import matplotlib.pyplot as plt

from londinium.parsing import get_datapaths, read_repo_data_files
from londinium.plotting.styles import line_colour_map, line_plot_order
from londinium.plotting.plotter import Canvas
from londinium.plotting.distortions import PolarDistortion


TFL_DATA_BASEDIR = '/mnt/c/Users/magic/Datasets/TfL'
REPO_DATA_BASEDIR = './data'

DPATHS = get_datapaths(
    tfl_data_basedir=TFL_DATA_BASEDIR,
    repo_data_basedir=REPO_DATA_BASEDIR
)


def main():
    
    (nr_lines, tfl_lines, nr_all_stations, nr_z16_stations, tfl_stations, disused_stations, osis) = read_repo_data_files(
        DPATHS.repo.lines.nr,
        DPATHS.repo.lines.tfl,
        DPATHS.repo.stations.nr.all,
        DPATHS.repo.stations.nr.z16,
        DPATHS.repo.stations.tfl,
        DPATHS.repo.stations.disused,
        DPATHS.repo.osis.json
    )


    tfl_lookup = {x.id:x for x in tfl_stations.stations}

    canvas = Canvas(distortion=PolarDistortion(),figsize=(20,30),
    dpi=150)

    for line in tfl_lines.lines:
        for link in line.links:
            canvas.plot(link.geometry,
                    color=line_colour_map[line.name].hex,
                    lw=1.2,
                    zorder=line_plot_order.index(line.name))

    for station in tfl_stations.stations:
        if len(station.lines) > 1 or station.name in osis.stations:
            color = '#FFFFFF'
            size = 4
            edge = '#000000'
            z = 98
        else:
            color = line_colour_map[station.lines[0]].hex
            size = 2
            edge = color
            z = line_plot_order.index(station.lines[0])

        canvas.plot(station.location,
                mfc=color,
                mec=edge,
                marker='o',
                ms=size,
                zorder=z)


    for station in disused_stations.stations:
        canvas.plot(station.location,
                mfc='#888888',
                mec='#888888',
                marker='o',
                ms=2,
                zorder=99)


    for osi in osis.osis:
        segment = [tfl_lookup[osi.a].location] + [tfl_lookup[osi.b].location]
        canvas.plot(segment,
                color='#000000',
                lw=3,
                zorder=97)
        canvas.plot(segment,
                color='#FFFFFF',
                lw=1,
                zorder=99)


    for nr_link in nr_lines.links:
        canvas.plot(
            nr_link.geometry,
            check_bbox=True,
            color='#DDDDDD',
            lw=1,
            zorder=line_plot_order.index('National Rail')
        )

    canvas.show()


if __name__ == '__main__':
    main()
