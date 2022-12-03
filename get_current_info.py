import requests

from secrets import get_aws_secret


# TODO: Change the class to use vraiables to create the data instead of all these methods.
# TODO: create some sort of class change or method to run all methods and return all data in a tuple of dict.
# TODO: Create a data engine to get this into a database / flow to see in bigeye

class SpaceDataTLE:

    def __init__(self, norad_id):
        self.api_root = 'https://api.n2yo.com/rest/v1/satellite/'
        self.api_key = get_aws_secret('api_key_n2yo')
        self.norad_id = norad_id

    def get_object_name(self):
        """This is used to return the two line element set decribing the position of the object associated with the
        NORAD ID passed. The NORAD ID is required, but can be found using another method in this class. """
        objact_data = requests.get(f'{self.api_root}tle/{self.norad_id}&apiKey={self.api_key}')
        return objact_data.json()['info']['satname']
    def get_object_tle(self):
        """This is used to return the two line element set decribing the position of the object associated with the
        NORAD ID passed. The NORAD ID is required, but can be found using another method in this class. """
        objact_data = requests.get(f'{self.api_root}tle/{self.norad_id}&apiKey={self.api_key}')
        return objact_data.json()['tle']

    def get_object_norad_id(self):
        """Get the NORAD classification of the object (U=unclassified, C= Classified, S=Secret)"""
        tle = self.get_object_tle()
        return tle[1:7].strip()

    def get_object_classification(self):
        """Get the NORAD classification of the object (U=unclassified, C= Classified, S=Secret)"""
        tle = self.get_object_tle()
        return tle[7]

    def get_object_international_designator_year(self):
        """Get the international designator for the year of the object's launch"""
        tle = self.get_object_tle()
        return int(tle[9:11].strip())

    def get_object_international_designator_launch(self):
        """Get the object's associated launch number for the year. E.G. a launch number of 067 neans this object was
        launched on the 67th launch of the year. """
        tle = self.get_object_tle()
        return int(tle[11:14].strip())

    def get_object_international_designator_piece(self):
        """Get the objects launch piece information. E.g. B would mean that this object was object B on that specific
        launch (A was anbother object on the launch) """
        tle = self.get_object_tle()
        return tle[14:17].strip()

    def get_object_epoch_year(self):
        """Get the EPOCH year of the launch. This is in EPOCH time format."""
        tle = self.get_object_tle()
        return tle[18:20].strip()

    def get_object_epoch_day(self):
        """Get the EPOCH day of the year. This is in EPOCH time format."""
        tle = self.get_object_tle()
        return float(tle[20:32].strip())

    def get_object_first_div(self):
        """First derivative of mean motion; the ballistic coefficient"""
        tle = self.get_object_tle()
        return tle[33:43].strip()

    def get_object_second_div(self):
        """Second derivative of mean motion; the ballistic coefficient"""
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


