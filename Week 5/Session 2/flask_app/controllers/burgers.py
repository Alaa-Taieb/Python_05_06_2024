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

@app.route('/burger/<int:id>/delete')
def delete_burger(id):
    data = {'id': id}
    Burger.delete(data)
    return redirect('/')

@app.route('/burger/<int:id>/update')
def update_page(id):
    # Get the burger from the database
    # Create the data dictionary
    data = {'id': id}
    burger = Burger.get_by_id(data)

    return render_template("update_burger.html" , burger = burger)


@app.route("/burger/update" , methods=['POST'])
def update():
    data = request.form
    Burger.update(data)
    return redirect('/')
