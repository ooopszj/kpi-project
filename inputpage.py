from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def page():
	return render_template('welcomepage.html')
# request is a part of Flask's HTTP requests

# methods is an array that's used in Flask which requests' methods are
# allowed to be performed in this route.
@app.route('/submitstuff', methods=['POST', 'GET'])
def submitstuff():
    # This is to make sure the HTTP method is POST and not any other
    if request.method == 'POST':
        # request.form is a dictionary that contains the form sent through
        # the HTTP request. This work by getting the name="xxx" attribute of
        # the html form field. So, if you want to get the name, your input
        # should be something like this: <input type="text" name="name" />.
        sd = request.form['sd']
        ed = request.form['ed']
        hn = request.form['hn']
        #result = request.form
		

        # This array is the fields your csv file has and in the following code
        # you'll see how it will be used. Change it to your actual csv's fields.
        fieldnames = ['sd', 'ed', 'hn']

        # We repeat the same step as the reading, but with "w" to indicate
        # the file is going to be written.
        with open('seih.csv','w', newline="") as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writeheader()

            # writerow() will write a row in your csv file
            writer.writerow({'sd': sd, 'ed': ed, 'hn': hn})

        # And you return a text or a template, but if you don't return anything
        # this code will never work.
        return render_template("tx.html")

    
'''@app.route("/")
def page():
	return render_template('welcomepage.html')
	
@app.route("/submitstuff", methods = ['GET', 'POST'])
def submitstuff():
	if request.method == 'POST':
		result = request.form
		print(result)
		return render_template("result.html",result = result)
@app.route('/')
def getinput():
	df = pd.read_csv('Copy of Super Template KPI.csv',sep=",", usecols= [5,8,9, 15,16,22,23,28, 29,30,31,32])
	dhi = df[(df['Month'] >= sd) & (df['Month'] <= ed) & (df['IMC'] == imc)& (df['Hauliers'] == hn)]
	if dhi == True:
	dhi.to_pickle('/users/ooops35/desktop/project/TOF.pkl')
'''
if __name__ == '__main__':
	app.run(debug = True)
