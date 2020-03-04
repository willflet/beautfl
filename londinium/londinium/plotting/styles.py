""" Plot configuration """

from ..colours import TfLColours as col

line_colour_map = {
    'Bakerloo': col.bakerloo,
    'Central': col.central,
    'Circle': col.circle,
    'District': col.district,
    'Hammersmith & City': col.hammersmith_and_city,
    'Jubilee': col.jubilee,
    'Metropolitan': col.metropolitan,
    'Northern': col.northern,
    'Piccadilly': col.piccadilly,
    'Victoria': col.victoria,
    'Waterloo & City': col.waterloo_and_city,
    'DLR': col.dlr,
    'Crossrail': col.elizabeth,
    'Crossrail 2': col.elizabeth,
    'Thameslink 6tph line': col.corporate_grey,
    'TfL Rail': col.tfl_rail,
    'Emirates Air Line': col.emirates,
    'East London': col.overground,
    'National Rail': col.corporate_grey,
    'London Overground': col.overground,
    'Tramlink': col.trams
}

line_plot_order = [
    'National Rail',
    'Crossrail',

    'Bakerloo',
    'Central',
    'Circle',
    'Hammersmith & City',
    'District',
    'Jubilee',
    'Metropolitan',
    'Northern',
    'Piccadilly',
    'Victoria',
    'Waterloo & City',

    'Crossrail 2',
    'Thameslink 6tph line',
    'Tramlink',
    'DLR',
    'London Overground',
    'East London',
    'TfL Rail',

    'Emirates Air Line',
]
