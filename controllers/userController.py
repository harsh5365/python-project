import sys
from flask import Response, jsonify, render_template, redirect, url_for, request, abort
from models.User import User
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def index():
    users = User.query.all()
    res = Response
    return jsonify([user.serialize for user in users])

def store():
    userData = request.get_json()
    print(userData)
    username = userData['username']
    age = userData['age']
    email = userData['email']
    gender = userData['gender']
    user = User(username=username, email=email, age=age, gender=gender)
    db.session.add(user)
    db.session.commit()
    return jsonify(message= "User Added Successfully")

def show(userId):
    user = User.query.get(userId)
    if user is None:
        abort(404)
    return render_template('show.html', user=user)

def update(userId):
    user = User.query.get(userId)
    if user is None:
        abort(404)
    name = request.form['name']
    age = request.form['age']
    address = request.form['address']
    user.name = name
    user.age = age
    user.address = address
    db.session.commit()
    return redirect(url_for('index'))

def delete(userId):
    user = User.query.get(userId)
    if user is None:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

def destroy(userId):
    user = User.query.get(userId)
    if user is None:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
