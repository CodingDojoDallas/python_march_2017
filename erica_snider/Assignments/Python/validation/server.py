from flask import Flask, render_template, request, redirect, session, flash
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():

    # NAME field with validation
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!") # just pass a string to the flash function
        session['name'] = "Name cannot be empty!"
    else:
        flash("Success! Your name is {}".format(request.form['name']))
        session['name'] = request.form['name']

    # LOCATION field without validation
    session['location'] = request.form['location']

    # LANGUAGE field without validation
    session['language'] = request.form['language']

    # COMMENT field with validation
    if len(request.form['comment']) < 1:
        flash("Comment cannot be empty!") # just pass a string to the flash function
        session['comment'] = "Name cannot be empty!"
    elif len(request.form['comment']) > 120:
        flash("Comment cannot be more than 120 characters!") # just pass a string to the flash function
        session['comment'] = "Comment cannot be more than 120 characters!"
    else:
        flash("Success! Your comment is {}".format(request.form['comment']))
        session['comment'] = request.form['comment']

    return redirect('/result') # alternatively, redirect to '/' to see the flash messages

@app.route('/result') # , methods=['GET']
def display_result():
    return render_template('results.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

@app.route('/back', methods=['POST'])
def back():
    session.pop('name')
    session.pop('location')
    session.pop('language')
    session.pop('comment')
    return redirect('/')

app.run(debug=True) # run our server
