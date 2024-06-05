import pandas as pd
from astroquery.vizier import Vizier
from astropy.coordinates import SkyCoord
from astropy import units as u
from intragen import raw1blgceph, raw1diskceph
import astropy.coordinates as coord
import statistics
import numpy as np

### Galactic Bulge Query ###

def queryblg(raw1blgceph):

    # Create a new empty column for distances
    raw1blgceph['Distance'] = None

    # Iterate through each row in the DataFrame
    for index, row in raw1blgceph.iterrows():
        ra = row['Ra']
        decl = row['Decl']

        try:
            # Connect to Vizier catalog
            v = Vizier(catalog="I/352", columns=['*', 'RA_ICRS', 'DE_ICRS'])

            # Query for nearby objects within 0.01 degrees radius by matching the radius of OGLE catalogue raw data to Bailer Jones GaiaDR3 Statistical Parallaxes Catalogue
            result = v.query_region(
                coord.SkyCoord(ra=ra, dec=decl, unit=(u.deg, u.deg), frame='icrs'),
                radius=0.01 * u.deg
            )

            # Sorting null and non-null results
            if len(result) > 0:
                # If results found, extract distance from the first object
                distance = result[0]['B_rgeo'][0]
                raw1blgceph.at[index, 'Distance'] = distance
            else:
                # If no results, set distance to None
                raw1blgceph.at[index, 'Distance'] = None

        except Exception as e:
            # Handle potential exceptions during Vizier query
            print(f"Error querying Vizier for row {index}: {e}")
            raw1blgceph.at[index, 'Distance'] = None  # Set distance to None for error cases

    return raw1blgceph

# Return distances into new dataframe with true distances
cleansedblgceph = queryblg(raw1blgceph.copy())  # Avoid modifying original DataFrame
print(cleansedblgceph)

### Galactic Disk Query ###

def querydisk(raw1diskceph):

    # Create a new empty column for distances
    raw1diskceph['Distance'] = None

    # Iterate through each row in the DataFrame
    for index, row in raw1diskceph.iterrows():
        ra = row['Ra']
        decl = row['Decl']

        try:
            # Connect to Vizier catalog
            v = Vizier(catalog="I/352", columns=['*', 'RA_ICRS', 'DE_ICRS'])

            # Query for nearby objects within 0.01 degrees radius 
            result = v.query_region(
                coord.SkyCoord(ra=ra, dec=decl, unit=(u.deg, u.deg), frame='icrs'),
                radius=0.01 * u.deg
            )

            # Sorting null and non-null results
            if len(result) > 0:
                # If results found, extract distance from the first object
                distance = result[0]['B_rgeo'][0]
                raw1diskceph.at[index, 'Distance'] = distance
            else:
                # If no results, set distance to None
                raw1diskceph.at[index, 'Distance'] = None

        except Exception as e:
            # Handle potential exceptions during Vizier query
            print(f"Error querying Vizier for row {index}: {e}")
            raw1diskceph.at[index, 'Distance'] = None  # Set distance to None for error cases

    return raw1diskceph

# Return distances into new dataframe with true distances
cleanseddiskceph = querydisk(raw1diskceph.copy())  # Avoid modifying original DataFrame
print(cleanseddiskceph)