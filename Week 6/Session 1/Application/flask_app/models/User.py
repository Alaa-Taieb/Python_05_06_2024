from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_bcrypt import Bcrypt
from flask import flash
from flask_app import app
import re

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.fullname = data['fullname']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # CRUD
    @classmethod
    def create(cls , data):
        """
            data = {
                'fullname': value,
                'email': value,
                'password': value("1234564")
            }
        """
        # hash the password before saving it in the database
        encrypted_password = bcrypt.generate_password_hash(data['password'])
        # Cast our immutable dictionary into a normal dictionary
        data = dict(data)
        # Updated the password
        data['password'] = encrypted_password
        query = "INSERT INTO users (fullname , email , password) VALUES(%(fullname)s , %(email)s , %(password)s);"
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod
    def get_by_email(cls , data):
        """
            data = {
                'email': value
            }
        """
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query , data)

        """
            results = ()
            results = ({})
        """
        if results == ():
            return False

        # return cls(results[0])

        user = cls(results[0])
        return user
    
    @staticmethod
    def validate_register(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if len(data['fullname']) <= 7:
            is_valid = False
            flash("Fullname must be at least 8 characters long.")
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid Email.")
        if user_in_db:
            is_valid = False
            flash("A user with this email already exists.")
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("Passwords must match.")
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_in_db = User.get_by_email(data)

        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email")
        if not user_in_db:
            is_valid = False
            flash("No user with this email exists.")
        elif not bcrypt.check_password_hash(user_in_db.password , data['password']):
            is_valid = False
            flash("Incorrect Password")
        
        return is_valid