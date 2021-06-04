from models.machine import Machine
from flask import request, jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MachineApi(Resource):
  def get(self, id = None):
    # id = machine_id
    if id is not None:
      return jsonify(Machine.query.filter_by(machine_id = id).all())
    stock = Machine.query.all()

    return jsonify(stock)

  def post(self):
    name = request.json['name']
    location = request.json['location']

    new_machine = Machine(name=name, location=location)
    db.session.add(new_machine)
    db.session.commit()

    return jsonify(new_machine)

  def put(self, id):
    # id = machine_id
    add = request.json['add']
    remove = request.json['remove']

    for item in add:
      Machine.query.filter_by(machine_id = id, product_id = item['product_id']).update({'quantity': Machine.quantity + item['quantity']})
    
    for item in remove:
      Machine.query.filter_by(machine_id = id, product_id = item['product_id']).update({'quantity': Machine.quantity - item['quantity']})
    
    db.session.commit()
    new_stock = Machine.query.filter_by(machine_id = id).all()

    return jsonify(new_stock)
