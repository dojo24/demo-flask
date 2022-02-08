from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.like import Likes
from flask_app.models.dislike import Dislikes
from flask_app.models.userLike import User_Likes

from  flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

# Register route
@app.route('/register', methods=['POST'])
def register():
    isValid = User.validate(request.form)
    if not isValid:
        return redirect('/')
    newUser = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'username': request.form['username'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(newUser)
    if not id:
        flash("Something went wrong!")
        return redirect('/')
    session['user_id'] = id
    return redirect('/dashboard')

# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = {
        'username': request.form['username']
    }
    user = User.getUsername(data)
    if not user:
        flash("Invalid Login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Wrong password")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')


@app.route('/logout/')
def logout():
    session.clear()
    flash("You have been logged out")
    return redirect('/')

@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in')
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        user = User.getOne(data)
        users = User.getAll()
        likes = Likes.getAll()
        dislikes = Dislikes.getAll()
        userLikes = User_Likes.getAll()
        return render_template('dashboard.html', user=user ,likes=likes, dislikes=dislikes, users=users, userLikes=userLikes)