from flask import Flask, render_template, request, redirect

app = Flask(__name__);

@app.route('/')
def index():
    return render_template("index.html")    # Render the template and return it

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       return render_template("result.html", result = request.form)

app.run(debug=True)                         # Run the app in debug mode
