from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.dislike import Dislikes
from flask_app.models.user import User
from flask_app.models.userDislike import User_Dislikes

@app.route('/dislike/create/', methods=['POST'])
def createDislike():
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'user_id': request.form['user_id'],
    }
    Dislikes.save(data)
    flash('Dislike created')
    print("printing data save from note controller: ", data)
    return redirect('/dashboard/')

@app.route('/dislike/agree/', methods=['POST'])
def userDislikeAgree():
    data = {
        'user_id': request.form['user_id'],
        'dislikes_id': request.form['dislikes_id'],
        'agreeCount': request.form['agreeCount']
    }
    User_Dislikes.saveAgree(data)
    flash('You agreed with something someone dislikes')
    print('printing data from userDislikeAgree controller: ', data)
    return redirect('/dashboard/')

@app.route('/dislike/disagree/', methods=['POST'])
def userDislikeDisagree():
    data = {
        'user_id': request.form['user_id'],
        'dislikes_id': request.form['dislikes_id'],
        'disagreeCount': request.form['disagreeCount']
    }
    User_Dislikes.saveDisagree(data)
    flash('You disagreed with something someone dislikes')
    print('printing data from userDislikeDisagree controller: ', data)
    return redirect('/dashboard/')