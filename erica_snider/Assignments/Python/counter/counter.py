from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    increment = 1
    session['counter'] += increment
    return render_template("index.html")

@app.route('/plus2', methods=['POST'])
def plus_two():
    increment = 1
    session['counter'] += increment
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True) # run our server
