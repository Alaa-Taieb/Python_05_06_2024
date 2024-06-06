from flask_app.config.mysqlconnection import DB , connectToMySQL
from flask_app.models.burger import Burger

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.quantity = data['quantity']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.burger = None

    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM orders JOIN burgers ON orders.burgers_id = burgers.id WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)

        """
            results = 
            [
                {
                    'id': 1,
                    'quantity': 25,
                    'created_at': "12-12-1970",
                    'updated_at': "12-12-1970",


                    'burgers.id': 2,
                    'name': "Name 2",
                    'bun': "Bun 2",
                    'meat': "meat 2",
                    'calories': "Calories 2",
                    'burgers.created_at': "created_at 2",
                    'burgers.updated_at': "updated_at 2",
                }
            ]
        """
        if results == []:
            return None
        order = cls(results[0])
        burger_data = {
            'id': results[0]['burgers.id'],
            'name': results[0]['name'],
            'bun': results[0]['bun'],
            'meat': results[0]['meat'],
            'calories': results[0]['calories'],
            'created_at': results[0]['burgers.created_at'],
            'updated_at': results[0]['burgers.updated_at']
        }
        order.burger = Burger(burger_data)
        return order



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders JOIN burgers ON orders.burgers_id = burgers.id;"
        results = connectToMySQL(DB).query_db(query)


        """
            results = 
            [
                {},{},{}
            ]
        """

        if results == []:
            return []
        
        orders = []
        for row in results:
            order = cls(row)
            burger_data = {
                'id': row['burgers.id'],
                'name': row['name'],
                'bun': row['bun'],
                'meat': row['meat'],
                'calories': row['calories'],
                'created_at': row['burgers.created_at'],
                'updated_at': row['burgers.updated_at']
            }
            order.burger = Burger(burger_data)
            orders.append(order)
        return orders # A list of Orders Objects



