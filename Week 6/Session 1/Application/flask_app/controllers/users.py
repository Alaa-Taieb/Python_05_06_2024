from flask import session , request , render_template , redirect
from flask_app.models.User import User
from flask_app import app

@app.route('/')
def index():
    if 'logged_user_email' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/register' , methods=['POST'])
def register():
    # request.form type is (ImmutableDict)
    data = request.form
    if User.validate_register(data):
        User.create(data)
    
    return redirect('/')

@app.route('/login' , methods=['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        session['logged_user_email'] = data['email']
        return redirect('/dashboard')

    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if not 'logged_user_email' in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')