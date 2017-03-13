import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# # routing rules and rest of server.py below
@app.route('/')
def index():
	
	if not "result" in session:
		session["result"] = ""
  	return render_template("games_index.html")

@app.route('/games', methods=['POST'])

def guess():
	guess = request.form["guess"]
	randomNumber = random.randint(0,101)
	print "session['result'] is:", session['result']

	if guess > randomNumber:
		result = "Too High"
		print "session['result'] is:", session['result']
	elif guess < randomNumber:
		result = "Too Low"
	else:
		result = "was the number!"
	# print "{}; was the number!".format(randomNumber)
	session['result'] = result
	print "this 2nd session['result'] is:", session['result']
	return redirect("/")   
# @app.route('/results')
# def show_user():
# 	return render_template('results.html')
app.run(debug=True)