import get_current_info
import database_dac
import database_engines

info = get_current_info.SpaceDataTLE(25544)

print(info.get_object_name())
print(info.get_object_tle())
print(info.get_object_classification())
print(info.get_object_norad_id())
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