#cannot plot the second haulier. no reason has been found
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv('MMW.csv', sep=",", index_col = None)
df = pd.read_csv('Copy of Super Template KPI.csv',sep=",", index_col = None)


a = df1.iloc[0,0]
b = df1.iloc[0,1]

h1 = df1.iloc[0,2]
h2 = df1.iloc[0,3]
h3 = df1.iloc[0,4]
h4 = df1.iloc[0,5]

pc = df[(df['Month'] >= a) & (df['Month'] <= b) & (df['Haulier'] == h1)]
pc = pc.to_pickle('/users/ooops35/desktop/project/haulier1.pkl')
dfc = pd.read_pickle('/users/ooops35/desktop/project/haulier1.pkl')

pdd = df[(df['Month'] >= a) & (df['Month'] <= b) & (df['Haulier'] == h2)]
pdd = pdd.to_pickle('/users/ooops35/desktop/project/haulier2.pkl')
dfd = pd.read_pickle('/users/ooops35/desktop/project/haulier2.pkl')



pe = df[(df['Month'] >= a) & (df['Month'] <= b) & (df['Haulier'] == h3)]
pe = pe.to_pickle('/users/ooops35/desktop/project/haulier3.pkl')
dfe = pd.read_pickle('/users/ooops35/desktop/project/haulier3.pkl')

pf = df[(df['Month'] >= a) & (df['Month'] <= b) & (df['Haulier'] == h4)]
pf = pf.to_pickle('/users/ooops35/desktop/project/haulier4.pkl')
dff = pd.read_pickle('/users/ooops35/desktop/project/haulier4.pkl')

dfc['Key'] = h1
dfd['Key'] = h2
dfe['Key'] = h3
dff['Key'] = h4

DF = pd.concat([dfc,dfd,dfe,dff],keys=[h1,h2,h3,h4])
DFGroup = DF.groupby(['Month', 'Key'])

DFGPlot = DFGroup.sum().unstack('Key').plot(kind='line',x_compat=True,y = ['On Time Arrival into MMW, %'])
DFGPlot1 = DFGroup.sum().unstack('Key').plot(kind='line',x_compat=True,y = ['On Time Despatch from MMW, %'])
#DFGPlot2 = DFGroup.sum().unstack('Key').plot(kind='line',x_compat=True,y = ['On Time to 1st Hub, %'])
#DFGPlotLFF = DFGroup.sum().unstack('Key').plot(kind='line',x_compat=True,y = ['Average LFF'])
DFGPlotap = DFGroup.sum().unstack('Key').plot(kind='line',x_compat=True,y = ['Average Pallets per Trip'])

DFGPlot.legend(loc='best')
DFGPlot1.legend(loc='best')
#DFGPlot2.legend(loc='best')
#DFGPlotLFF.legend(loc='best')
DFGPlotap.legend(loc='best')



plt.title('MMWOTArrival')
fig = DFGPlot.get_figure()
fig.savefig("/users/ooops35/desktop/project/static/MMWOTArrival.png",bbox_inches='tight')

plt.title('MMWOTDespatch')
fig = DFGPlot1.get_figure()
fig.savefig("/users/ooops35/desktop/project/static/MMWOTDespatch.png",bbox_inches='tight')

#fig = DFGPlot2.get_figure()
#fig.savefig("/users/ooops35/desktop/project/static/1sthub.png",bbox_inches='tight')
#fig = DFGPlotLFF.get_figure()
#fig.savefig("/users/ooops35/desktop/project/static/averagelff.png",bbox_inches='tight')

plt.title('Averagepallets')
fig = DFGPlotap.get_figure()
fig.savefig("/users/ooops35/desktop/project/static/averagepallets.png",bbox_inches='tight')

plt.style.use('ggplot')
plt.show()
