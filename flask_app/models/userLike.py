from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.like import Likes
from flask_app.models.user import User

class User_Likes:
    db='display'
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.dislike_id = data['dislike_id']
        self.agreeCount = data['agreeCount']
        self.disagreeCount = data['disagreeCount']

    @classmethod
    def saveAgree(cls, data):
        q = 'INSERT INTO user_likes (user_id, like_id, agreeCount) VALUES (%(user_id)s, %(like_id)s, %(agreeCount)s);'
        return connectToMySQL(cls.db).query_db(q, data)
    
    @classmethod
    def saveDisagree(cls, data):
        q = 'INSERT INTO user_likes (user_id, like_id, disagreeCount) VALUES (%(user_id)s, %(like_id)s, %(disagreeCount)s);'
        return connectToMySQL(cls.db).query_db(q, data)
    
    @classmethod
    def getAll(cls):
        q = 'SELECT * FROM user_likes;'
        r = connectToMySQL(cls.db).query_db(q)
        userLikes = []
        for row in r:
            userLikes.append(cls(row))
        return userLikes