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

# Importing true distance value dataset

from query import truedist

# Due to the iteration process and distance filling - rows of truedist = rows of queried dataset






# ROUND 3: Mode seperation of datasets --> Dataset generation complete










