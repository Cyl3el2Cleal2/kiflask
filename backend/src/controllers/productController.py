from models.product import Product
from flask import request, jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProductApi(Resource):
  def get(self):
    products = Product.query.all()

    return jsonify({
        'count': len(products),
        'data': jsonify(products)
    })

  def post(self):
    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']

    new_product = Product(name=name, price=price, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()

    return jsonify(new_product)