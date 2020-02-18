# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 23:18:08 2020

@author: chakati
"""

import pandas as pd
import numpy as np
import urllib.request, json 

#load Data
with urllib.request.urlopen(r"https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets") as url:
    df = pd.DataFrame.from_dict(json.loads(url.read().decode()), orient='columns')
    
    

#Question 1
orphan_planets = df[df['TypeFlag'] == 3]
print('orphan_planets')
print(orphan_planets['PlanetIdentifier'])

#question 2
df['HostStarTempK'] = df.apply(lambda x: np.nan if x['HostStarTempK'] == '' else x['HostStarTempK'], axis = 1)
Hotteststar=df[df['HostStarTempK'] == df['HostStarTempK'].max()]['PlanetIdentifier']
#print('Name of the planet orbiting hottest star:\n', df[df['HostStarTempK'] == df['HostStarTempK'].max()]['PlanetIdentifier'])
print('Name of the planet orbiting hottest star:\n',Hotteststar);

#question 3

df['RadiusJpt'] = df.apply(lambda x: np.nan if x['RadiusJpt'] == '' else x['RadiusJpt'], axis = 1)
def size(x):
    if x['RadiusJpt'] == np.nan:
        return "null"
    elif x['RadiusJpt'] < 1:
        return "small"
    elif ((x['RadiusJpt'] >= 1) & (x['RadiusJpt'] < 2)):
        return "medium"
    elif x['RadiusJpt'] >= 2:
        return "large"

df['size'] = df.apply(size, axis = 1)


df['DiscoveryYear'] = df.apply(lambda x: np.nan if x['DiscoveryYear'] == '' else x['DiscoveryYear'], axis = 1)
df1=df.groupby(['DiscoveryYear', 'size']).count()['PlanetIdentifier']
