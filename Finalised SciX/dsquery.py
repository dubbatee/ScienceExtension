import pandas as pd
from astroquery.vizier import Vizier
from astropy.coordinates import SkyCoord
from astropy import units as u
from intragen import raw1blgds, raw1diskds
import astropy.coordinates as coord
import statistics
import numpy as np

### Galactic Bulge Query ###

def queryblg(raw1blgds):

    # Create a new empty column for distances
    raw1blgds['Distance'] = None

    # Iterate through each row in the DataFrame
    for index, row in raw1blgds.iterrows():
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
                raw1blgds.at[index, 'Distance'] = distance
            else:
                # If no results, set distance to None
                raw1blgds.at[index, 'Distance'] = None

        except Exception as e:
            # Handle potential exceptions during Vizier query
            print(f"Error querying Vizier for row {index}: {e}")
            raw1blgds.at[index, 'Distance'] = None  # Set distance to None for error cases

    return raw1blgds

# Return distances into new dataframe with true distances
cleansedblgds = queryblg(raw1blgds.copy())  # Avoid modifying original DataFrame
print(cleansedblgds)

### Galactic Disk Query ###

def querydisk(raw1diskds):

    # Create a new empty column for distances
    raw1diskds['Distance'] = None

    # Iterate through each row in the DataFrame
    for index, row in raw1diskds.iterrows():
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
                raw1diskds.at[index, 'Distance'] = distance
            else:
                # If no results, set distance to None
                raw1diskds.at[index, 'Distance'] = None

        except Exception as e:
            # Handle potential exceptions during Vizier query
            print(f"Error querying Vizier for row {index}: {e}")
            raw1diskds.at[index, 'Distance'] = None  # Set distance to None for error cases

    return raw1diskds

# Return distances into new dataframe with true distances
cleanseddiskds = querydisk(raw1diskds.copy())  # Avoid modifying original DataFrame
print(cleanseddiskds)





        

    