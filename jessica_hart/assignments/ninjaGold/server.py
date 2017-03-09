from flask import Flask, render_template, redirect, request, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'abkjlkhkljhklhlkjhlkc'

@app.route('/')
def index():
    if not 'gold' in session:       # If no gold is in session, set gold to 0
        session['gold'] = 0
    if not 'events' in session:     # Initialize events list if not in session
        session['events'] = []
    return render_template('index.html')

@app.route('/process_gold', methods=['POST'])
def process_gold():
    building = request.form['building']     # Generate gold range based on building
    if building == 'Farm':
        result = random.randint(10, 21)
        session['gold'] += result
    elif building == 'Cave':
        result = random.randint(5, 11)
        session['gold'] += result
    elif building == 'House':
        result = random.randint(2, 6)
        session['gold'] += result
    elif building == 'Casino':
        result = random.randrange(-50, 51)
        session['gold'] += result

    timestamp = datetime.now().strftime('%Y/%m/%d %-I:%S %p')
    if result < 0:
        act_string = 'Entered a {} and lost {} gold... Ouch.. ({})'.format(building, abs(result), timestamp)
        rg_class = 'red'
    else:
        act_string = 'Earned {} gold from the {}! ({})'.format(result, building, timestamp)
        rg_class = 'green'
    event = {                   # Pass both the string to print and the desired color class
		'msg': act_string,
		'class': rg_class,
	}
    session['events'].insert(0, event)

    return redirect('/')

app.run(debug=True)
