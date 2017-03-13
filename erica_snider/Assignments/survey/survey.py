from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    # recall the name attributes we added to our form inputs
    # to access the data that the user input into the fields we use request.form['name_of_input']
    global name, location, language, comment
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    # redirects back to the '/' route
    return redirect('/result')

@app.route('/result') # , methods=['GET']
def display_result():
    print "Results"
    print name
    return render_template('results.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True) # run our server
