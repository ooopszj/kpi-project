import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#df1 = pd.read_csv('seih.csv', sep=",", index_col = None)
df = pd.read_csv('inmarket.csv',sep=",",usecols=(0,1,4,5,6,7,8,9), index_col = None)
#df.tail(n = 2).to_html('TOF&TM.html', index = False)

#current month 
def getinput():
    currentmonth = input('enter a start date: ')
    imcname = input('enter a carrier\'s name: ') 
    imcname1 = input('enter a carrier\'s name: ') 
    imc1 = df[(df['Month'] >= currentmonth) & (df['IMC'] == imcname)]
    imc2 = df[(df['Month'] >= currentmonth) & (df['IMC'] == imcname1)]
    imc1.to_pickle('/users/ooops35/desktop/project/imc1.pkl')
    imc2.to_pickle('/users/ooops35/desktop/project/imc1.pkl')
    print(imc1)
    print(imc2)
	   
getinput()


imc1 = pd.read_pickle('/users/ooops35/desktop/project/imc1.pkl')
imc1_plot = imc1.plot(kind = 'bar', x = ['IMC'],y = ['Number of Parcels', 'Number of Pallets'])
fig = imc1_plot.get_figure()
fig.savefig('/users/ooops35/desktop/project/static/tof.png')
plt.show()

