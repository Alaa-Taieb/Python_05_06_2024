from flask_app.config.mysqlconnection import DB , connectToMySQL

class Burger:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # CRUD
    # READ - GET ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        results = connectToMySQL(DB).query_db(query)

        """
            results = 
            [
                {
                    'id': 1,
                    'name': "Name 1",
                    'bun': "Bun 1",
                    'meat': "meat 1",
                    'calories': "Calories 1",
                    'created_at': "created_at 1",
                    'updated_at': "updated_at 1",
                }
                ,
                {
                    'id': 2,
                    'name': "Name 2",
                    'bun': "Bun 2",
                    'meat': "meat 2",
                    'calories': "Calories 2",
                    'created_at': "created_at 2",
                    'updated_at': "updated_at 2",
                }
            ]
        """
        
        if results == []:
            return []
        burgers = []
        for row in results:
            burger = cls(row)
            burgers.append(burger)
            # burgers.append(cls(row))
        return burgers
    
    # READ - GET BY ID
    @classmethod
    def get_by_id(cls , data):
        """
            data = 
            {
                'id': 2
            }
        """
        query = "SELECT * FROM burgers WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)

        """
            results = [] - no record exists with the provided ID
            results = 
            [
                {
                    'id': 2,
                    'name': "Name 2",
                    'bun': "Bun 2",
                    'meat': "meat 2",
                    'calories': "Calories 2",
                    'created_at': "created_at 2",
                    'updated_at': "updated_at 2",
                }
            ]
        """
        if results == []:
            return None
        burger = cls(results[0])
        return burger
        # return cls(results[0])

    # CREATE
    @classmethod
    def create(cls , data):
        query = "INSERT INTO burgers (name , bun , meat , calories) VALUES(%(name)s , %(bun)s , %(meat)s , %(calories)s);"
        return connectToMySQL(DB).query_db(query , data)
