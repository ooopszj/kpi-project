import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Copy of Super Template KPI.csv',sep=",",usecols=(0,1,9))

def getinput():
    c = input('enter a start date: ')
    b= input('enter a end date: ')
    d = input('enter the first haulier: ')
    hauliername = df[(df['Month'] >= c) & (df['Month'] <= b) & (df['Haulier'] == d)]
    
    d1 = input('enter second haulier: ')
    hauliername1 = df[(df['Month'] >= c) & (df['Month'] <= b) &(df['Haulier'] == d1)]
    
    d2 = input('enter third haulier: ')
    hauliername2 = df[(df['Month'] >= c) & (df['Month'] <= b) &(df['Haulier'] == d2)]
    
    d3 = input('enter fourth haulier: ')
    hauliername3 = df[(df['Month'] >= c) & (df['Month'] <= b) &(df['Haulier'] == d3)]
    
    hauliername.to_pickle('/users/ooops35/desktop/project/h0.pkl')
    hauliername1.to_pickle('/users/ooops35/desktop/project/h1.pkl')
    hauliername2.to_pickle('/users/ooops35/desktop/project/h2.pkl')
    hauliername3.to_pickle('/users/ooops35/desktop/project/h3.pkl')
    
    
    #give a range for the hauliers list. 
getinput()

df0 = pd.read_pickle('/users/ooops35/desktop/project/h0.pkl')
df1 = pd.read_pickle('/users/ooops35/desktop/project/h1.pkl')
df2 = pd.read_pickle('/users/ooops35/desktop/project/h2.pkl')
df3 = pd.read_pickle('/users/ooops35/desktop/project/h3.pkl')

df0['Key'] = 'a'
df1['Key'] = 'b'
df2['Key'] = 'c'
df3['Key'] = 'd'

DF = pd.concat([df0,df1,df2,df3],keys=['a','b','c','d'])

DFGroup = DF.groupby(['Month', 'Key'])

DFGPlot = DFGroup.sum().unstack('Key').plot(kind='line',x_compat=True,)

#fig = DFGPlot.get_figure()
#fig.savefig("/users/ooops35/desktop/project/static/planVSactual.png")

plt.style.use('ggplot')
plt.show()

#sort
#def sortBykey():
   # sbk = sorted(a.items(), key = lambda t: t[0])
  #  print(sbk)
#how to flatten list of list 
#for i, j in enumerate(a):
    #print(i,j)
#if a[ == 'Jan-14': # if a[][]==input string: 
    #print(a[0][:13])

#print(type(a[0][1]))



#df = pd.read_csv('Copy of Super Template KPI.csv',index_col = 'Month',parse_dates = True)
#print(df)

#df2 = df['Planning Performance']

#print(df2.head())#head()only list the first five data
#a = df.values.T.tolist()  

#print(a)

#df = df.drop_duplicates(subset = 'Month', keep = 'last')
"""
reader = csv.reader(open('Copy of Super Template KPI.csv'))

results = {}
for row in reader:#
    key = row[0]
    if key in results:
        pass
    results[key] = row[1:]
#print (results)

for key, value in results.items():
    if key == 'Jan-14':
        #print(key, value[0])
       


# open the file in universal line ending mode 
with open('Copy of Super Template KPI.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

# extract the variables you want
month = data['Month']
pp = data['Planning Performance']


plt.xlabel('month')
plt.ylabel('pp')
plt.show()


#pp = df1.plot(kind = 'line', x=["Month"],y = ['On Time Arrival into MMW, %'],legend=None)
#fig = pp.get_figure()
#fig.savefig("/users/ooops35/desktop/project/static/oooh.png")
#order by month column 
#print(a['Month'])
#df3=df2.astype(float)

#ax = df1.plot(kind = 'line', x=["Month"],sharex = True)
#df3.plot(ax = ax)

"""