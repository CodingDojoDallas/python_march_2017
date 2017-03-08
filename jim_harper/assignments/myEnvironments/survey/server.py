from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'harper'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html', name = session['name'], location = session['location'], language = session['language'], comment = ['comment'])

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')


app.run(debug=True)
