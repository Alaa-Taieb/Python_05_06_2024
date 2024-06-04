from flask_app import app


from flask import render_template , redirect , request
from flask_app.models.burger import Burger

@app.route('/')
def home():
    data = Burger.get_all()
    return render_template('index.html' , burgers = data)

@app.route('/burgers' , methods=['POST'])
def create_burger():
    print(request.form)
    Burger.create(request.form)
    return redirect('/')