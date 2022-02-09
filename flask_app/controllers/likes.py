from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.like import Likes
from flask_app.models.user import User
from flask_app.models.userLike import User_Likes

@app.route('/like/create/', methods=['POST'])
def createLike():
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'user_id': request.form['user_id'],
    }
    Likes.save(data)
    flash('Like created')
    print("printing data save from like controller, line 14, likes.py: ", data)
    return redirect('/dashboard/')

@app.route('/like/agree/', methods=['POST'])
def userLikeAgree():
    data = {
        'user_id': request.form['user_id'],
        'likes_id': request.form['likes_id'],
        'agreeCount': request.form['agreeCount']
    }
    User_Likes.saveAgree(data)
    flash('You agreed with something someone likes')
    print('printing data from userLikeAgree controller: ', data)
    return redirect('/dashboard/')

@app.route('/like/disagree/', methods=['POST'])
def userLikeDisagree():
    data = {
        'user_id': request.form['user_id'],
        'likes_id': request.form['likes_id'],
        'disagreeCount': request.form['disagreeCount']
    }
    User_Likes.saveDisagree(data)
    flash('You disagreed with something someone likes')
    print('printing data from userLikeDisagree controller: ', data)
    return redirect('/dashboard/')
