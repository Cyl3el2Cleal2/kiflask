from models.stock import Stock
from flask import request, jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class StockApi(Resource):
    def get(self, id=None):
        # id = machine_id
        if id is not None:
            return jsonify(Stock.query.filter_by(machine_id=id).all())
        stock = Stock.query.all()

        return jsonify(stock)

    def post(self, id=None):
        product_id = request.json['product_id']
        quantity = request.json['quantity']

        new_stock = Stock(
            machine_id=id, product_id=product_id, quantity=quantity)
        db.session.add(new_stock)
        db.session.commit()

        return jsonify(new_stock)

    def put(self, id):
        # id = machine_id
        add = request.json['add']
        remove = request.json['remove']

        new_items = []
        for item in add:
            # check is exist
            isExist = Stock.query.filter_by(
                machine_id=id, product_id=item['product_id']).all()
            if len(isExist) == 0:
                # insert
                new_items.append(
                    Stock(machine_id=id, product_id=item['product_id'], quantity=item['quantity']))
            else:
                current_stock = Stock.query.filter_by(machine_id=id, product_id=item['product_id']).first()
                current_stock.quantity = current_stock.quantity + item['quantity']

        for item in remove:
            current_stock = Stock.query.filter_by(machine_id=id, product_id=item['product_id']).first()
            current_stock.quantity = current_stock.quantity - item['quantity']
            
            if current_stock.quantity < 10:
              # Send Signal to admin if quantity < 10
              pass
            

        db.session.add_all(new_items)
        db.session.commit()
        new_stock = Stock.query.filter_by(machine_id=id).all()

        return jsonify(new_stock)
