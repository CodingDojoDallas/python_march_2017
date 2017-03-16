from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import random
import re # the "re" module will let us perform some regular expression operations
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriendsdb')
app.secret_key = 'ThisIsSecret'

# try making validation function separate from an app.route; call inside of app.routes when needed

@app.route('/')
def index():
    # Display all of the friends on the index.html page
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)


@app.route('/friends', methods=['POST'])
def create():
    # Handle the add friend form submit and create the friend in the DB

    validated = 1

    # FIRST NAME validation
    if len(request.form['first_name']) < 1:
        flash("First name cannot be empty!")
        validated = 0

    # LAST NAME validation
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be empty!")
        validated = 0

    # EMAIL validation
    if len(request.form['email']) < 1:
        flash("Email cannot be empty!")
        validated = 0
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email address must be valid!")
        validated = 0

    # if everything passes validation, add information to database
    if validated == 1:
        query = "INSERT INTO fullfriendsdb.friends (first_name, last_name, email) VALUES (:first_name, :last_name, :email)"
        print query
        data = {
                    'first_name': request.form['first_name'],
                    'last_name': request.form['last_name'],
                    'email': request.form['email']
                }
        mysql.query_db(query, data)

    return redirect('/')


@app.route('/friends/<id>/edit')
def edit(id):
    # Display the edit friend page for the particular friend

    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': id}
    friends = mysql.query_db(query, data)
    return render_template('edit.html', one_friend=friends[0])


@app.route('/friends/<id>', methods=['POST'])
def update(id):
    # Handle the edit friend form submit and update the friend in the DB

    validated = 1
    # Only update fields that have information entered; blank fields remain original value
    if request.form['first_name']:
        query = "UPDATE friends SET first_name = :first_name WHERE id = :specific_id"
        data = {
                    'specific_id': id,
                    'first_name': request.form['first_name'],
                }
        friends = mysql.query_db(query, data)
    if request.form['last_name']:
        query = "UPDATE friends SET last_name = :last_name WHERE id = :specific_id"
        data = {
                    'specific_id': id,
                    'last_name': request.form['last_name'],
                }
        friends = mysql.query_db(query, data)
    if request.form['email']:
        if not EMAIL_REGEX.match(request.form['email']):
            flash("Email address must be valid!")
            validated = 0
        else:
            query = "UPDATE friends SET email = :email WHERE id = :email"
            data = {
                        'specific_id': id,
                        'email': request.form['email'],
                    }
            friends = mysql.query_db(query, data)

    return redirect('/')


@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    # Delete the friend from the DB
    query = "DELETE FROM friends WHERE id = :specific_id"
    data = {'specific_id': id}
    friends = mysql.query_db(query, data)

    return redirect('/')


app.run(debug=True)
