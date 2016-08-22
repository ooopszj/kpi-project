import pandas as pd
import matplotlib

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter
import math
plt.style.use('ggplot')
pp = pd.read_csv('Copy of Super Template KPI.csv')
pp1 = pp.drop_duplicates(subset = 'Month', keep = 'last')

#print(pp1)
"""set bar range
low =min(pp['Planning Performance'])
high = max(pp['Planning Performance'])                   
plt.ylim([math.ceil(low-0.5*(high-low)), math.ceil(high+0.5*(high-low))])
"""
pp_plot = pp1.plot(kind="bar",x=["Month"],y = ['Planning Performance'],legend=None)


matplotlib.use('Agg')

#plt.show()
fig = pp_plot.get_figure()

fig.savefig("/users/ooops35/desktop/project/static/h.png")

#print(plt.style.available)