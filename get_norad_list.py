import csv
import datetime
from codecs import iterdecode
from contextlib import closing

import requests
import urllib3
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

from database_dac import NORADInfo
import database_dac
import database_engines
metadata = MetaData()
row_number = 0
source_csv = 'https://celestrak.org/pub/satcat.csv'
with requests.Session() as s:
    download = s.get(source_csv)
    engine = database_engines.engine_postgres(database='Space', echo=True)
    decoded_content = download.content.decode('utf-8')
    session = Session(engine)
    database_dac.Base.metadata.create_all(engine)
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    next(cr, None)
    row_list = list(cr)
    for row in row_list:
        row_number += 1

        # Correct NULL values
        for cell in range(len(row)):
            if row[cell] == '':
                row[cell] = None
            norad_record = NORADInfo(
                id=row[2],
                record_time=datetime.datetime.now(),
                object_name=row[0],
                object_id=row[1],
                object_type=row[3],
                ops_status_code=row[4],
                owner=row[5],
                launch_date=row[6],
                launch_site=row[7],
                decay_date=[8],
                period=row[9],
                inclination=row[10],
                apogee=row[11],
                perigee=row[12],
                rcs=[13],
                data_status_code=row[14],
                orbit_center=row[14],
                orbit_type=row[16],
            )
            session.add(norad_record)
    session.commit()
    session.close()
