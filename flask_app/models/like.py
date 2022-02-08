from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Likes:
    db='display'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.user_id = data['user_id']


    @classmethod
    def save(cls, data):
        q = 'INSERT INTO likes (name, description, user_id) VALUES (%(name)s, %(description)s, %(user_id)s);'
        return connectToMySQL(cls.db).query_db(q, data)

    @classmethod
    def getAll(cls):
        q = 'SELECT * FROM likes;'
        r = connectToMySQL(cls.db).query_db(q)
        like = []
        for row in r:
            like.append(cls(row))
        return like

    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM likes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
