from flask_app import app
from flask import render_template , request , redirect , session

from flask_app.models.Review import Review
from flask_app.models.User import User

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    user_data = {'id': session['user_id']}
    logged_user = User.get_by_id(user_data)
    reviews = Review.get_all()
    return render_template("dashboard.html" , logged_user = logged_user , reviews = reviews)

@app.route('/review/add-review')
def add_review_page():
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template("add_review.html" , logged_user  = logged_user)

@app.route('/review/create' , methods=['POST'])
def add_review():
    data = request.form
    Review.create(data)
    return redirect('/dashboard')

@app.route('/review/<int:id>/delete')
def delete_review(id):
    data = {'id': id}
    Review.delete(data)
    return redirect('/dashboard')

@app.route('/review/<int:id>/edit')
def edit_review_page(id):
    data = {'id': id}
    review = Review.get_by_id(data)
    return render_template("edit_review.html" , review = review)

@app.route("/review/update" , methods=['POST'])
def update_review():
    data = request.form
    Review.update(data)
    return redirect('/dashboard')

@app.route('/review/<int:id>/show')
def show_review_page(id):
    review = Review.get_by_id({'id': id})
    return render_template("show_review.html" , review = review)
