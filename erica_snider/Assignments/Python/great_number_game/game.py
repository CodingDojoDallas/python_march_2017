from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if not 'random_num' in session:
        session['random_num'] = random.randrange(0,101)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])

    print "session['guess'] is:", session['guess']

    if session['random_num'] == session['guess']:
        session['match'] = "Win"
    else:
        if session['guess'] > session['random_num']:
            session['match'] = "Too high!"
        else:
            session['match'] = "Too low!"
    return redirect('/')

@app.route('/play_again', methods=['POST'])
def again():
    session.pop('random_num')
    session.pop('match')
    # print "session is ", session
    return redirect('/')

app.run(debug=True) # run our server
