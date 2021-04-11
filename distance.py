from math import radians, cos, sin, asin, sqrt

#https://github.com/mapado/haversine/blob/master/tests/test_haversine.py
class Distance:

    def __init__(self, earth, office):
        self.earth = earth
        self.office = office
    #Returns distance in KMs
    def get_km(self,la,lo):

        # unpack latitude/longitude
        lat1, lng1 = self.office
        lat2 = float(la)
        lng2 = float(lo)

        #Validating ranges https://docs.mapbox.com/help/glossary/lat-lon/#
        if not (-90.0 <= lat2 <= 90.0):
            raise Exception('Latitude out of range')

        if not (-180.0 <= lng2 <= 180.0):
            raise Exception('Latitude out of range')

        # convert all latitudes/longitudes from decimal degrees to radians
        lat1 = radians(lat1)
        lng1 = radians(lng1)
        lat2 = radians(lat2)
        lng2 = radians(lng2)

        # calculate haversine
        lat = lat2 - lat1
        lng = lng2 - lng1
        d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2

        return int(2 * self.earth  * asin(sqrt(d)))
