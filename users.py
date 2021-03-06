from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Users;"
        results = connectToMySQL('user_cr_2').query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO Users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        results =  connectToMySQL('user_cr_2').query_db(query, data)
        return results
