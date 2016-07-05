import os
import pandas as pd
import csv
import glob
import seaborn as sns
import matplotlib.pyplot as plot
import numpy as np
import json
from pandas.io.json import json_normalize


collectionpath="/home/shahbaz/Comments"

data = json.load(collectionpath)
df= json_normalize(data)
print (df.head(n=10))

