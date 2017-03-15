from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['ninjas'] = {
        'blue': 'donatello.jpg',
        'orange': 'Michelangelo',
        'red': 'Raphael',
        'purple': 'Donatello'
    }
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    session['color'] = ['blue','orange','red','purple']
    print session['ninjas']['blue']
    return render_template("ninja.html")

@app.route('/ninja/<color>')
def color(color):
    # session['color'] = ['blue','orange','red','purple']
    # session['color'] = session['ninjas']['<color>']
    # session['color'] = session['ninjas']['blue']
    print session['ninjas']['blue']
    return render_template("ninja.html", color=color)

app.run(debug=True)
