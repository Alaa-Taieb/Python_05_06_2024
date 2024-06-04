from flask import Flask , render_template , request , redirect , session

app = Flask(__name__)
app.secret_key = "sdlfhjeaslouid;fhujeso"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/display_info')
def display():
    
    return render_template('info.html')

@app.route('/submit_info' , methods=['POST'])
def submit_info():
    session['first_name'] = request.form['first_name']
    session['second_name'] = request.form['second_name']
    session['age'] = request.form['age']
    return redirect('/display_info')

if __name__ == "__main__":
    app.run(debug=True)