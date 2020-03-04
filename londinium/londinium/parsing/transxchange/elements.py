""" For parsing TransXChange xml files. Deliberately incomplete. """


class TXCStopPoint(object):
    def __init__(self, e, ns):
        self.id = e.findtext('ns:AtcoCode', namespaces=ns)
        self.name = e.find('ns:Descriptor', namespaces=ns).findtext('ns:CommonName', namespaces=ns)

        self.locality = e.findtext('./ns:Place/ns:NptgLocalityRef', namespaces=ns)
        self.location = (e.findtext('./ns:Place/ns:Location/ns:Easting', namespaces=ns), e.findtext('./ns:Place/ns:Location/ns:Northing', namespaces=ns))


class TXCRouteSection(object):
    def __init__(self, e, ns):
        self.id = e.get('id')
        self.route_links = [self.TXCRouteLink(x, ns) for x in e.findall('ns:RouteLink', namespaces=ns)]

    class TXCRouteLink(object):
        def __init__(self, e, ns):
            self.id = e.get('id')
            self.fra = e.findtext('./ns:From/ns:StopPointRef', namespaces=ns)
            self.to = e.findtext('./ns:To/ns:StopPointRef', namespaces=ns)
            self.distance = e.findtext('ns:Distance', namespaces=ns)
            self.direction = e.findtext('ns:Direction',namespaces= ns)


class TXCRoute(object):
    def __init__(self, e, ns):
        self.id = e.get('id')
        self.code = e.findtext('ns:PrivateCode', namespaces=ns)
        self.description = e.findtext('ns:Description', namespaces=ns)
        self.route_sections = [x.text for x in e.findall('ns:RouteSectionRef', namespaces=ns)]


class TXCService(object):
    def __init__(self, e, ns):
        self.id = e.findtext('ns:ServiceCode', namespaces=ns)
        self.private_code = e.findtext('ns:PrivateCode', namespaces=ns)

        lines = e.findall('./ns:Lines/ns:Line', namespaces=ns)
        if len(lines) > 1:
            raise ValueError('More than one Line present!')
            # self.lines = [self.TXCLine(x) for x in e.findall('Lines/Line')]
        else:
            self.line = self.TXCLine(lines[0], ns)

        self.start_date = e.findtext('./ns:OperatingPeriod/ns:StartDate', namespaces=ns)
        self.end_date = e.findtext('./ns:OperatingPeriod/ns:EndDate', namespaces=ns)

        self.operator = e.findtext('ns:RegisteredOperatorRef', namespaces=ns)

        self.description = e.findtext('ns:Description', namespaces=ns)

        if any((l.id != self.id) for l in [self.line]):
            raise ValueError('line ids do not match')

        if self.private_code != self.id:
            raise ValueError('code does not match')

    class TXCLine(object):
        def __init__(self, e, ns):
            self.id = e.get('id')
            self.name = e.findtext('ns:LineName', namespaces=ns)
