# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 20:29:17 2016

@author: ooops35
"""

import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv('seih.csv', sep=",", index_col = None)
df = pd.read_csv('inmarket.csv',sep=",",usecols=(0,1,11,13,14,16,17), index_col = None)


a = df1.iloc[0,0]
b = df1.iloc[0,1]
c = df1.iloc[0,2]
#if a in df1['Month'].to_string() and b in df1['Month'].to_string() and c in df1['IMC'].to_string():
p = df[(df['Month'] >= a) & (df['Month'] <= b) & (df['IMC'] == c)]
p = p.to_pickle('/users/ooops35/desktop/project/test.pkl')

dff = pd.read_pickle('/users/ooops35/desktop/project/test.pkl')
dff.plot(kind = 'line', x = ['Month'],y = ['Total In Full, %', 'Carrier-related On Time, %','OT Target, %','IF Target, %'])
plt.show()
