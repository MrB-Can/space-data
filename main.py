import requests
from json import JSONDecodeError


class SpaceData:
    def __init__(self, norad_id):
        self.api_root = 'https://api.n2yo.com/rest/v1/satellite/'
        self.api_key = '25544&apiKey=R9CBTT-75U9QA-GCFB86-4YNB'
        self.norad_id = norad_id

    def get_object_tle(self):
        """This is used to return the two line element set decribing the position of the object associated with the
        NORAD ID passed. The NORAD ID is required, but can be found using another method in this class. """
        object_position = requests.get(f'{self.api_root}tle/{self.norad_id}&apiKey={self.api_key}')
        return object_position.json()['tle']

    def get_object_classification(self):
        """Get the NORAD classification of the object (U=unclassified, C= Classified, S=Secret)"""
        tle = self.get_object_tle()
        return tle[7]

    def get_object_international_designator_year(self):
        """Get the NORAD classification of the object (U=unclassified, C= Classified, S=Secret)"""
        tle = self.get_object_tle()
        return int(tle[9:11].strip())

    def get_object_international_designator_launch(self):
        """Get the NORAD classification of the object (U=unclassified, C= Classified, S=Secret)"""
        tle = self.get_object_tle()
        return int(tle[11:14].strip())

    def get_object_international_designator_piece(self):
        """Get the NORAD classification of the object (U=unclassified, C= Classified, S=Secret)"""
        tle = self.get_object_tle()
        return tle[14:17].strip()

    def get_object_epoch_year(self):
        """Get the NORAD classification of the object (U=unclassified, C= Classified, S=Secret)"""
        tle = self.get_object_tle()
        return tle[18:20].strip()

    def get_object_epoch_day(self):
        """Get the NORAD classification of the object (U=unclassified, C= Classified, S=Secret)"""
        tle = self.get_object_tle()
        return float(tle[20:32].strip())

    def get_object_first_div(self):
        """First derivative of mean motion; the ballistic coefficient"""
        tle = self.get_object_tle()
        return tle[33:43].strip()

    def get_object_second_div(self):
        """First derivative of mean motion; the ballistic coefficient"""
        tle = self.get_object_tle()
        return tle[44:52].strip()

    def get_object_drag(self):
        """B*, the drag term, or radiation pressure coefficient (decimal point assumed)"""
        tle = self.get_object_tle()
        return tle[53:61].strip()

    def get_object_element_set(self):
        """Element set number. Incremented when a new TLE is generated for this object"""
        tle = self.get_object_tle()
        return tle[64:68].strip()

    def get_object_inclination(self):
        """Inclination (degrees)"""
        tle = self.get_object_tle()
        return tle[78:87].strip()

    def get_object_ascension(self):
        """Right ascension of the ascending node (degrees)"""
        tle = self.get_object_tle()
        return tle[88:96].strip()

    def get_object_eccentricity(self):
        """Eccentricity (decimal point assumed)	"""
        tle = self.get_object_tle()
        return tle[97:105].strip()

    def get_object_perigee(self):
        """Argument of perigee (degrees)	"""
        tle = self.get_object_tle()
        return tle[105:114].strip()

    def get_object_anomaly(self):
        """Argument of perigee (degrees)	"""
        tle = self.get_object_tle()
        return tle[114:122].strip()

    def get_object_motion(self):
        """Mean motion (revolutions per day)	"""
        tle = self.get_object_tle()
        return tle[122:134].strip()

    def get_object_revolutions(self):
        """Mean motion (revolutions per day)	"""
        tle = self.get_object_tle()
        return tle[134:139].strip()

info = SpaceData(25544)
print(info.get_object_tle())
print(info.get_object_classification())
print(info.get_object_international_designator_year())
print(info.get_object_international_designator_launch())
print(info.get_object_international_designator_piece())
print(info.get_object_epoch_year())
print(info.get_object_first_div())
print(info.get_object_second_div())
print(info.get_object_drag())
print(info.get_object_inclination())
print(info.get_object_ascension())
print(info.get_object_eccentricity())
print(info.get_object_perigee())
print(info.get_object_anomaly())
print(info.get_object_motion())
print(info.get_object_revolutions())
