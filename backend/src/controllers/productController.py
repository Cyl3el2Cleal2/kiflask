from models.product import Product
from flask import request, jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ProductApi(Resource):
  def get(self, id = None):
    if id is not None:
      return jsonify(Product.query.filter_by(id = id).first())
    products = Product.query.all()

    return jsonify(products)

  def post(self):
    name = request.json['name']
    price = request.json['price']
    img = request.json['img']

    new_product = Product(name=name, price=price, img=img)
    db.session.add(new_product)
    db.session.commit()

    return jsonify(new_product)