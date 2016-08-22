import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('inmarket.csv',sep=",",usecols=(1,4,5,6,7,8,9),index_col = False)
df = df.tail(2)
htmltable = df.to_html('average.html')


df1 = pd.read_csv('inmarket.csv',sep=",",usecols=(1,34,35),index_col = False)
df1 = df1.tail(2)
TOF = df1.head(1)
TM = df1.tail(1)


TOFline = TOF.convert_objects(convert_numeric=True)
#TOFline = TOF['Average Weight per Order']
TOF.plot(kind = 'line')

#print(TOFline)

'''TOF.plot(kind = 'bar', x = ['IMC'], 
         y = ['Number of Pallets','Number of Parcels'],
         secondary_y = ['Number of Parcels'], ax = ax)

TM.plot(kind = 'bar', x = ['IMC'], 
         y = ['Number of Pallets','Number of Parcels'],
         secondary_y = ['Number of Parcels'], ax= ax)
#TM.plot(kind = 'bar')
'''
plt.show()

