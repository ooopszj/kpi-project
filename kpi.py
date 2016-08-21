from flask import *
import jinja2
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/hello")
def pic():
	return render_template('hello.html')

@app.route("/hello")
def ppchart():
	plt.style.use('ggplot')
	pp = pd.read_csv('Copy of Super Template KPI.csv')
	pp1 = pp.drop_duplicates(subset = 'Month', keep = 'last')
	pp_plot = pp1.plot(kind="bar",x=["Month"],y = ['Planning Performance'],legend=None)
	fig = pp_plot.get_figure()
	fig.savefig("/users/ooops35/desktop/project/static/h.png")
	return render_template('hello.html')


@app.route("/")
def hello():
    df = pd.read_csv('Copy of Super Template KPI.csv',sep=",", usecols= [5,8,9, 15,16,22,23,28, 29,30,31,32])
    df1 = df.tail(4)
    return render_template('hello.html', df = df1.to_html(index = False))

@app.route("/hello")
def pachart():
	plt.style.use('ggplot')
	pa = pd.read_csv('Copy of Super Template KPI.csv')
	pp_plot = pa.plot(kind="line",x=["Month"],y = ['On Time Arrival into MMW, %'],legend=None)
	fig = pp_plot.get_figure()
	fig.savefig("/users/ooops35/desktop/project/static/planVSactual.png")
	return render_template('hello.html')

@app.route("/hello")
def TOFontime():
	#plt.style.use('ggplot')
	df = pd.read_csv('inmarket.csv',sep=",",usecols=(0,1,11,13,14,16,17), index_col = None)
	dff = pd.read_pickle('/users/ooops35/desktop/project/TOF.pkl')
	dff.plot(kind = 'line', x = ['Month'],y = ['Total In Full, %', 'Carrier-related On Time, %','OT Target, %','IF Target, %'])
	fig = pp_plot.get_figure()
	fig.savefig("/users/ooops35/desktop/project/static/TOF.png")

	dff = dff.T
	dff = dff.drop(dff.index[[1]])
	return render_template('hello.html')



if __name__ == '__main__':
	app.run(debug = True)