from flask import Flask , render_template , request, session , redirect
import requests

app = Flask(__name__)
app.secret_key = "skdufheksdfe"

@app.route('/')
def index():

    return render_template("index.html")

@app.route("/get_flag" , methods=['POST'])
def handle_flag_response():
    name = request.form['country_name']
    url = f"https://restcountries.com/v3.1/name/{name}?fields=flags"

    response = requests.get(url)
    data = response.json()

    session['flag_url'] = data[0]['flags']['png']

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)