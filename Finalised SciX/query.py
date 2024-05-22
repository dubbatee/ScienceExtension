from astroquery.vizier import Vizier
import astropy.units as u
import astropy.coordinates as coord
from astroquery.gaia import Gaia
import pandas as pd
import numpy as np
import matplotlib as plt
from astropy.time import Time
from intragen import raw1blgds

for index, row in raw1blgds.iterrows():
    v = Vizier(catalog="I/352", columns=['*', 'RA_ICRS','DE_ICRS'])#.query_constraints(RA_ICRS=row["Ra"])[0]
    result = v.query_region(coord.SkyCoord(ra=row['Ra'], dec=row['De'],
                                            unit=(u.deg, u.deg),
                                            frame='icrs'),
                        radius=0.0001*u.deg,
                        catalog=["I/352"])
    
    if (len(result) == 0):
        distance = 0
    else:
        distance = result[0]['rgeo'][0]
        cleansedbgds.loc[len(cleansedbgds.index)] = [row['ID'],row['Ra'],row['De'], row['I'], row['V'], row['V-I'], row['P'], result[0]['rgeo'][0]] 