import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('inmarket.csv',sep=",",usecols=(0,1,11,13,14,16,17), index_col = None)

def getinput():
    c = input('enter a start date: ')
    b = input('enter a end date: ')
    d = input('enter the first haulier: ')
    hauliername = df[(df['Month'] >= c) & (df['Month'] <= b) & (df['IMC'] == d)]
    #print(hauliername)
    hauliername.to_pickle('/users/ooops35/desktop/project/TOF.pkl')
    print(type(c))
getinput()
dff = pd.read_pickle('/users/ooops35/desktop/project/TOF.pkl')
dff.plot(kind = 'line', x = ['Month'],y = ['Total In Full, %', 'Carrier-related On Time, %','OT Target, %','IF Target, %'])
plt.show()


#dff.reset_index( drop=False, inplace=True )
#dff.reindex_axis(['Month','Total In Full, %', 'Carrier-related On Time, %','OT Target, %','IF Target, %'], axis=1)

dff = dff.T
dff = dff.drop(dff.index[[1]])
print(dff)

dff.to_html('12333.html',header=False)


