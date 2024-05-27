from flask import Flask , render_template


app = Flask(__name__)


@app.route('/')
def root_route():
    return render_template("index.html")

@app.route("/anotherRoute")
def another_route():
    return "This is another route"


@app.route("/greet/<string:name>/<string:color>")
def greet(name , color):
    animals = ["Dog" , "Cat" , "Snake" , "Lion" , "Gnat"]
    return render_template("greet.html" , var1 = name , color = color , animals = animals)


if __name__ == "__main__":
    app.run(debug=True)