import numpy as np
import pandas as pd
import json

with open('IMG_1753.json') as json_data:
    data = json.load(json_data)


inputpoints = np.zeros((len(data['vertices']), 2))

for i in range(0,len(data['vertices']),1):
    inputpoints[i,:] = data['vertices'][i]['point']
