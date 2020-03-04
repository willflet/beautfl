""" Colours for visualization.

The values for TfL's colours are taken from their
`colour standard <http://content.tfl.gov.uk/tfl-colour-standards-issue04.pdf>`_
and `style guide <http://content.tfl.gov.uk/design-style-guide.pdf>`_ documents.
"""


class Colour(object):
    """ Container for colour values. """

    def __init__(self, pms=None, cmyk=None, rgb=None, ncs=None):
        """ Make a new colour object. """

        if pms is not None: pms = str(pms).zfill(3)
        if cmyk is not None: cmyk = tuple(cmyk)
        if rgb is not None: rgb = tuple(rgb)

        self._pms = pms
        self._cmyk = cmyk
        self._rgb = rgb
        self._ncs = ncs

    def __call__(self, pms=None, cmyk=None, rgb=None, ncs=None):
        """ Make a new colour, perhaps with changed attributes. """

        pms = pms or self.pms
        cmyk = cmyk or self.cmyk
        rgb = rgb or self.rgb
        ncs = ncs or self.ncs

        return self.__class__(pms=pms, cmyk=cmyk, rgb=rgb, ncs=ncs)

    def __str__(self):
        return self.hex

    @property
    def hex(self):
        return '#{:02x}{:02x}{:02x}'.format(*self.rgb)

    @property
    def pms(self):
        return self._pms

    @property
    def cmyk(self):
        return self._cmyk

    @property
    def rgb(self):
        return self._rgb

    @property
    def ncs(self):
        return self._ncs


class TfLColours(object):
    """ Data class containing official TfL colours. """
    # Corporate colours
    corporate_blue = Colour(pms=72, cmyk=(100,88,0,5), rgb=(0,25,168), ncs='S 3560-R80B')
    corporate_red = Colour(pms=485,cmyk=(0,95,100,0),rgb=(220,36,31), ncs='S 1085-Y80R')
    corporate_grey = Colour(pms=43, cmyk=(5,0,0,45), rgb=(134,143,152), ncs='S 4005-R80B')
    corporate_dark_grey = Colour(pms=432, cmyk=(23,2,0,77), rgb=(65,75,86), ncs='S 7010-R90B')
    corporate_yellow = Colour(pms=116, cmyk=(0,16,100,0), rgb=(255,206,0), ncs='S 0580-Y10R')
    corporate_green = Colour(pms=356, cmyk=(95,0,100,27), rgb=(0,114,41), ncs='S 3065-G10Y')
    corporate_black = Colour(pms='Black', cmyk=(0,0,0,100), rgb=(0,0,0), ncs='S 9000-N')
    corporate_white = Colour(cmyk=(0,0,0,0), rgb=(255,255,255), ncs='S 0500-N')

    # Mode specific colours
    tfl = corporate_blue(ncs='S 4060-R80B')
    emirates = Colour(pms=186, cmyk=(0,100,81,4), rgb=(220,36,31))
    buses = corporate_red()
    coaches = Colour(pms=130, cmyk=(0,30,100,0), rgb=(241,171,0), ncs='S1070-Y20R')
    elizabeth = Colour(pms=266, cmyk=(73,81,0,0), rgb=(147,100,204))
    santander = Colour(cmyk=(0,93,100,0), rgb=(220,36,31))
    dial_a_ride = Colour(pms='Pantone Purple', cmyk=(38,88,0,0), rgb=(183,39,191), ncs='S 2050-R40B')
    dlr = Colour(pms=326, cmyk=(87,0,38,0), rgb=(0,175,173), ncs='S 2050-B50G')
    overground = Colour(pms=158, cmyk=(0,61,97,0), rgb=(239,123,16), ncs='S 0585-Y50R')
    riverboat = Colour(pms=299, cmyk=(85,19,0,0), rgb=(0,160,226), ncs='S 2060-B')
    taxi = Colour(pms=2715, cmyk=(57,45,0,0), rgb=(132,128,215), ncs='S 2060-R70B')
    tfl_rail = tfl()
    trams = Colour(pms=368, cmyk=(57,0,100,0), rgb=(0,189,25), ncs='S 0580-G30Y')
    underground = tfl()
    visitor_centre = Colour(cmyk=(0,100,0,0), rgb=(220,0,107))

    # Safety colours
    safety_blue = Colour(pms=300, cmyk=(100,57,4,0), rgb=(0,96,168), ncs='S 3065-R90B')

    # London Underground line colours
    bakerloo = Colour(pms=470, cmyk=(26,67,89,19), rgb=(178,99,0), ncs='S 4050-Y50R')
    central = corporate_red()
    circle = corporate_yellow()
    district = corporate_green()
    hammersmith_and_city = Colour(pms=197, cmyk=(2,50,17,0), rgb=(244,169,190), ncs='S 0550-R10B')
    jubilee = Colour(pms=430, cmyk=(53,37,34,16), rgb=(161,165,167), ncs='S 4005-R80B')
    metropolitan = Colour(pms=235, cmyk=(38,100,27,27), rgb=(155,0,88), ncs='S 4050-R30B')
    northern = corporate_black()
    piccadilly = tfl()
    victoria = Colour(pms=299, cmyk=(80,15,0,0), rgb=(0,152,216), ncs='S 2060-B')
    waterloo_and_city = Colour(pms=338, cmyk=(57,0,40,0), rgb=(147,206,186), ncs='S 1565-B')

    # Other logos and identities
    congestion_charging = Colour(pms=186, cmyk=(0,100,81,4), rgb=(210,16,52), ncs='S 1080-Y90R')
    cycle_superhighway = Colour(pms=214, cmyk=(0,100,34,8), rgb=(220,9,99))
    legible_london_blue = Colour(cmyk=(87,46,0,81), rgb=(6,26,48))
    legible_london_yellow = Colour(cmyk=(0,22,100,6), rgb=(240,187,0))
    low_emission_zone = Colour(pms=370, cmyk=(56,0,100,27), rgb=(82,186,0))
    oyster_blue = Colour(pms=72, cmyk=(100,88,0,5), rgb=(134,143,152), ncs='S 3560-R80B')
    oyster_cyan = Colour(pms='Cyan', cmyk=(100,0,0,0), rgb=(0,157,217), ncs='S 1565-B')

    # Style guide extras
    primary_blue = Colour(rgb=(26,90,146))
    dark_grey_blue = Colour(rgb=(45,48,57))
    modified_tfl_blue = Colour(rgb=(17,59,146))
    turquoise = Colour(rgb=(102,204,204))

    accent_light_grey_1 = Colour(rgb=(247,247,247))
    accent_light_grey_2 = Colour(rgb=(238,238,238))
    accent_mid_grey = Colour(rgb=(204,204,204))
    accent_light_blue = Colour(rgb=(239,246,253))
    accent_mid_blue = Colour(rgb=(204,221,232))
    accent_green = Colour(rgb=(231,246,220))
    accent_warning_yellow = Colour(rgb=(250,245,225))
    accent_error_red = Colour(rgb=(255,239,239))

    london_streets = Colour(rgb=(151,166,155))
