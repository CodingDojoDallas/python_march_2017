from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re # the "re" module will let us perform some regular expression operations
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'emaildb')

@app.route('/')
def index():
    query = "SELECT * FROM email"                           # define your query
    email = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_email=email) # pass data to our template     all_friends=friends

@app.route('/validate', methods=['POST'])
def validateAndCreate():

    # EMAIL validation
    if len(request.form['email']) < 1:
        flash("Email cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email address must be valid!")
    else:
        flash("Success! Your email is {}".format(request.form['email']))
        # on successful validation, insert email into database and redirect to success page
        query = "INSERT INTO emaildb.email (`email`) VALUES (:email)"
        print query
        data = { 'email': request.form['email'] }
        mysql.query_db(query, data)
        return redirect('/success')

    # on failed validation, redirect to index page to display flash message
    return redirect('/')

@app.route('/success')
def show():
    query = "SELECT * FROM email"
    email = mysql.query_db(query)
    return render_template('success.html', all_email=email)

app.run(debug=True)
