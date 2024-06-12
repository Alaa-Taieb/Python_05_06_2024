
from flask_app.config.mysqlconnection import DB , connectToMySQL
from flask_app.models.User import User

class Review:
    def __init__(self ,data):
        self.id = data['id']
        self.title = data['title']
        self.rating = data['rating']
        self.date_watched = data['date_watched']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.user = None


    # ! CURD Operations
    # READ
    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM reviews JOIN users ON reviews.user_id = users.id WHERE reviews.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)

        """
            results =
                (
                    {
                        'id': value,
                        'title': value,
                        'rating': value,
                        'content': value,
                        'date_watched': value,
                        'created_at': value,
                        'updated_at': value,
                        'user_id': value,
                        'users.id': value,
                        'email': value,
                        'first_name': value,
                        'last_name': value,
                        'password': value,
                        'users.created_at': value,
                        'users.updated_at': value
                    }
                )

            results = ()
        """
        if not results:
            return None
        review = cls(results[0])
        user_data = {
            'id': results[0]['users.id'],
            'email': results[0]['email'],
            'first_name': results[0]['first_name'],
            'last_name': results[0]['last_name'],
            'password': results[0]['password'],
            'created_at': results[0]['users.created_at'],
            'updated_at': results[0]['users.updated_at']
        }
        review.user = User(user_data)
        return review
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM reviews JOIN users ON reviews.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query)

        if not results:
            return []
        reviews = []
        for row in results:
            review = cls(row)
            user_data = {
                'id': row['users.id'],
                'email': row['email'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            review.user = User(user_data)
            reviews.append(review)
        return reviews
    
    @classmethod
    def create(cls , data):
        query = "INSERT INTO reviews (title , rating , date_watched , content , user_id) VALUES(%(title)s , %(rating)s , %(date_watched)s , %(content)s , %(user_id)s);"
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod
    def update(cls , data):
        query = "UPDATE reviews SET title = %(title)s , rating = %(rating)s ,date_watched = %(date_watched)s ,content = %(content)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod
    def delete(cls , data):
        query = "DELETE FROM reviews WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)