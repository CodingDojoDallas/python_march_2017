from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re # the "re" module will let us perform some regular expression operations
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
mysql = MySQLConnector(app,'wall')
app.secret_key = 'ThisIsSecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt = Bcrypt(app)

def validate_first_name(first_name):
    if len(first_name) < 1:
        flash("First name cannot be empty.")
        return False
    else:
        return True

def validate_last_name(last_name):
    if len(last_name) < 1:
        flash("Last name cannot be empty.")
        return False
    else:
        return True

def validate_email(email):
    if len(email) < 1:
        flash("Email cannot be empty.")
        return False
    elif not EMAIL_REGEX.match(email):
        flash("Email address must be valid.")
        return False
    else:
        return True

def validate_password(password):
    if len(password) < 1:
        flash("Password cannot be empty.")
        return False
    elif len(password) < 8:
        flash("Password must be at least 8 characters.")
        return False
    else:
        return True

def validate_password_conf(password, password_conf):
    if password != password_conf:
        flash("Passwords must match.")
        return False
    return True

@app.route('/')
def index():
    if 'id' in session:
        return redirect('/wall')
    else:
        query = "SELECT * FROM users"
        users = mysql.query_db(query)
        return render_template('index.html', all_users=users)

@app.route('/register', methods=['POST'])
def create():
    # Handle the registration form submit and create the user in the db
    if validate_first_name(request.form['first_name']) and validate_last_name(request.form['last_name']) and validate_email(request.form['email']) and validate_password(request.form['password']) and validate_password_conf(request.form['password'], request.form['password_conf']):
        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)
        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        print query
        data = {
                    'first_name': request.form['first_name'],
                    'last_name': request.form['last_name'],
                    'email': request.form['email'],
                    'pw_hash': pw_hash
                }
        mysql.query_db(query, data)

        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        query_data = { 'email': request.form['email'] }
        user = mysql.query_db(user_query, query_data)
        session['id'] = user[0]['id']
        return redirect('/wall')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    if validate_email(request.form['email']) and validate_password(request.form['password']):
        email = request.form['email']
        password = request.form['password']
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        query_data = { 'email': email }
        user = mysql.query_db(user_query, query_data) # user will be returned in a list
        print "this is the user: ", user
        if len(user) > 0:
            if bcrypt.check_password_hash(user[0]['pw_hash'], password):
                # login user
                session['id'] = user[0]['id']
                return render_template('wall.html')
        else:
            # set flash error message and redirect to login page
            flash("Email or password is incorrect.")
    return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('id')
    return redirect('/')

@app.route('/message', methods=['POST'])
def message():
    query = "INSERT INTO messages (users_id, message, created_at, updated_at) VALUES (:users_id, :message, NOW(), NOW())"
    data = {
                'users_id': session['id'],
                'message': request.form['message']
            }
    mysql.query_db(query, data)
    print "this is the message ", request.form['message']
    return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
    query = "INSERT INTO comments (messages_id, users_id, comment, created_at, updated_at) VALUES (:messages_id, :users_id, :comment, NOW(), NOW())"
    data = {
                'messages_id': request.form['message_id'],
                'users_id': session['id'],
                'comment': request.form['comment']
            }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/wall')
def wall():

    query= "SELECT m.id, u.first_name, u.last_name, m.created_at, m.message \
            FROM messages AS m \
            JOIN users AS u \
            ON u.id=m.users_id \
            ORDER BY m.created_at DESC"
    all_messages = mysql.query_db(query)

    query= "SELECT c.id, c.messages_id, u.first_name, u.last_name, c.created_at, c.comment \
            FROM comments AS c \
            JOIN users AS u  \
            ON u.id=c.users_id  \
            ORDER BY c.created_at ASC"
    all_comments = mysql.query_db(query)

    # query = "SELECT * FROM users"  # would this make all the data available to the users if it was passed into render_template? 
    # users = mysql.query_db(query)
    #
    # query = "SELECT * FROM messages"
    # messages = mysql.query_db(query)
    #
    # query = "SELECT * FROM comments"
    # comments = mysql.query_db(query)

    return render_template('wall.html', all_messages=all_messages, all_comments=all_comments)  # , users=users, all_info=all_info

app.run(debug=True)
