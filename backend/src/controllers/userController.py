from flask import request, jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserApi(Resource):
  def post(self):
    username = request.json['name']
    email = request.json['email']
    new_user = User(username=username, email=email)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)