from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)

class User:

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    def __init__(self , data):
        self.id = data['id']
        self.email = data['email']
        self.fullname = data['fullname']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls , data):
        # Encrypt the password
        encrypted_password = bcrypt.generate_password_hash(data['password'])
        data = dict(data)
        data['password'] = encrypted_password

        query = "INSERT INTO users (fullname , password , email) VALUES(%(fullname)s, %(password)s , %(email)s);"
        return connectToMySQL(DB).query_db(query , data)

    
    @classmethod
    def get_by_id(cls , data):
        """
            data = {
                'id': value,
                ...
            }
        """
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)

        if result:
            return cls(result[0])
        return None
    
    @classmethod
    def get_by_email(cls , data):
        """
            data = {
                'email': value,
                ...
            }
        """
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query , data)

        if result:
            return cls(result[0])
        return None
    

    @staticmethod
    def validate_register(data):
        """
            data = {
                'fullname': value,
                'email': value,
                'password': value,
                'confirm_password': value
            }
        """
        is_valid = True
        user_in_db = User.get_by_email(data)
        if len(data['fullname']) < 7:
            flash("Register: Full name needs to be longer than 6 characters")
            is_valid = False
        if not User.EMAIL_REGEX.match(data['email']):
            flash("Register: Invalid Email.")
            is_valid = False
        if user_in_db:
            flash("Register: This email is already used.")
            is_valid = False
        if len(data['password']) < 8:
            flash("Register: Password must at least be 8 characters long.")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Register: Passwords must match.")
            is_valid = False

        return is_valid
    
    @staticmethod
    def validate_login(data):
        """
            data = {
                'email': value,
                'password': value
            }
        """
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not User.EMAIL_REGEX.match(data['email']):
            flash("Login: Invalid Email.")
            is_valid = False
        if not user_in_db:
            flash("Login: No user exists in this database.")
            is_valid = False
        elif not bcrypt.check_password_hash(user_in_db.password , data['password']):
            flash("Login: Incorrect Password.")
            is_valid = False
    
        return is_valid

