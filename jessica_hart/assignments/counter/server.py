from flask import Flask, render_template, redirect, session

app = Flask(__name__);
app.secret_key = 'Ywhhkt^1i@812T6M8!C5!t3*'

@app.route('/')
def index():
    if not 'count' in session:       # If no count is in session, set count to 0
        session['count'] = 0
    else:
        session['count'] += 1       # Add to count on every refresh/redirect to index
    # try:                          # Alternative way to doing the above condition
    #     session['count'] += 1
    # except KeyError:
    #     session['count'] = 0
    return render_template("index.html")

@app.route('/countup', methods = ['POST'])
def countup():
   session['count'] += 1            # Add only 1 because index will add another 1
   return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
   session['count'] = 0             # Reset to 0 and index will set to 1
   return redirect('/')

app.run(debug=True)
