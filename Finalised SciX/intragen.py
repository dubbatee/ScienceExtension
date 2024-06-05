import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy import stats

### imported metadata from the OGLE IV Catalogue of Delta Scuti Variables into pandaS dataframes ###

#Galactic Bulge Delta Scuti Variable Dataframe - Raw
rawblgds = pd.read_csv ('blgdsdata.csv')
rawblgds.columns = ['ID', 'mode', 'Ra', 'Decl', 'I', 'V', 'V-I', 'P1', 'P2']

#Galactic Disk Delta Scuti Variable Dataframe - Raw
rawdiskds = pd.read_csv ('diskdsdata.csv')
rawdiskds.columns = ['ID', 'mode', 'Ra', 'Decl', 'I', 'V', 'V-I', 'P1', 'P2']

### imported metadata from the OGLE IV Catalogue of Classical Cepheid Variables into pandaS dataframes ###

#Galactic Bulge Classical Cepheid Variable Dataframe - Raw 
rawblgceph = pd.read_csv ('blgcephdata.csv')
rawblgceph.columns = ['ID', 'mode', 'Ra', 'Decl', 'I', 'V', 'V-I', 'P1']

#Galactic Disk Classical Cepheid Variable Dataframe - Raw
rawdiskceph = pd.read_csv ('diskcephdata.csv')
rawdiskceph.columns = ['ID', 'mode', 'Ra', 'Decl', 'I', 'V', 'V-I', 'P1']

### data cleaning/pre-processing ###

# ROUND 1: apparent magnitude thresholding - based on OGLE IV telescope saturation and sensitivity limits

#Delta Scuti Variables

rawblgds = rawblgds[rawblgds['I'] > 13]
raw1blgds = rawblgds[rawblgds['I'] < 21.5]

rawdiskds = rawdiskds[rawdiskds['I'] > 13]
raw1diskds = rawdiskds[rawdiskds['I'] < 21.5]

#Classical Cepheid Variables

rawblgceph = rawblgceph[rawblgceph['I'] > 13]
raw1blgceph = rawblgceph[rawblgceph['I'] < 21.5]

rawdiskceph = rawdiskceph[rawdiskceph['I'] > 13]
raw1diskceph = rawdiskceph[rawdiskceph['I'] < 21.5]

# ROUND 2: distance query availability - If a star's true or most accurately known distance is unable to queried from the Bailer Jones 2021 Gaia DR3 Statistical Parallax Catalogue (Queried via vizier.)
# Querying process done in "query.py" 

# Importing "Cleansed" Dataframes from Galactic Bulge and Galactic Disk for both Classical Cepheids and Delta Scutis

from dsquery import cleansedblgds, cleanseddiskds
from cephquery import cleansedblgceph, cleanseddiskceph

# ROUND 3: Mode seperation of datasets

## Delta Scuti Data frames ##

#Galactic Bulge Dataframes

Fundamentalblgds = cleansedblgds.drop(cleansedblgds[cleansedblgds['P2'] != (-99.99)].index)

FirstOvertoneblgds = cleansedblgds.drop(cleansedblgds[cleansedblgds['mode'] == ('singlemode')].index)

#Galactic Disk Dataframes

Fundamentaldiskds = cleanseddiskds.drop(cleanseddiskds[cleanseddiskds['P2'] != (-99.99)].index)

FirstOvertonediskds = cleanseddiskds.drop(cleanseddiskds[cleanseddiskds['mode'] == ('singlemode')].index)

## Classical Cepheid Data frames ##

#Galactic Bulge Dataframes

Fundamentalblgceph = cleansedblgceph.drop(cleansedblgceph[cleansedblgceph['mode'] != ('F')].index)

FirstOvertoneblgceph = cleansedblgceph.drop(cleansedblgceph[cleansedblgceph['mode'] == ('F')].index)

#Galactic Disk Dataframes

Fundamentaldiskceph = cleanseddiskceph.drop(cleanseddiskceph[cleanseddiskceph['mode'] != ('F')].index)

FirstOvertonediskceph = cleanseddiskceph.drop(cleanseddiskceph[cleanseddiskceph['mode'] == ('F')].index)

#dataframes exported back to distance calculation files






