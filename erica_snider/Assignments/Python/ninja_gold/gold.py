from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if not 'total_gold' in session:
        session['total_gold'] = 0
    if not 'activity_log' in session:
        session['activity_log'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def guess():
    win_lose = 1 # winning gold
    building = request.form['building']
    if building == 'farm':
        session['gold'] = random.randrange(10,21)
        building = request.form['building']
    elif building == 'cave':
        session['gold'] = random.randrange(5,11)
    elif building == 'house':
        session['gold'] = random.randrange(2,6)
    elif building == 'casino':
        session['gold'] = random.randrange(0,51)
        earn_or_take = random.randrange(0,2)
        if earn_or_take == 0:
            session['gold'] *= -1
            win_lose = 0 # losing gold
    print session['gold']
    session['total_gold'] += session['gold']

    if win_lose == 1:
        session['activity_log'].append("Earned " + str(session['gold']) + " golds from the " + building + "!")
    else:
        session['activity_log'].append("Entered a casino and lost " + str(session['gold']*-1) + " golds... Ouch.. ")

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('activity_log')
    session.pop('total_gold')
    return redirect('/')

app.run(debug=True) # run our server
