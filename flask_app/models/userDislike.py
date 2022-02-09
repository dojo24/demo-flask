from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.dislike import Dislikes
from flask_app.models.user import User

class User_Dislikes:
    db='display'
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.dislikes_id = data['dislikes_id']
        self.agreeCount = data['agreeCount']
        self.disagreeCount = data['disagreeCount']

    @classmethod
    def saveAgree(cls, data):
        q = 'INSERT INTO user_dislikes (user_id, dislikes_id, agreeCount) VALUES (%(user_id)s, %(dislikes_id)s, %(agreeCount)s);'
        return connectToMySQL(cls.db).query_db(q, data)
    
    @classmethod
    def saveDisagree(cls, data):
        q = 'INSERT INTO user_dislikes (user_id, dislikes_id, disagreeCount) VALUES (%(user_id)s, %(dislikes_id)s, %(disagreeCount)s);'
        return connectToMySQL(cls.db).query_db(q, data)

    @classmethod
    def getAll(cls):
        q = 'SELECT * FROM user_dislikes;'
        r = connectToMySQL(cls.db).query_db(q)
        userDislikes = []
        for row in r:
            userDislikes.append(cls(row))
        return userDislikes