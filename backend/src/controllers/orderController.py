from models.order import Order
from models.order_detail import OrderDetail
from dataclasses import asdict
from flask import request, jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class OrderApi(Resource):
    def get(self, id = None):
      if id is None:
        Orders = Order.query.all()
        result = []
        for order in Orders:
          order = asdict(order)
          order['order_details'] = OrderDetail.query.filter_by(order_id = order['id']).all()
          result.append(order)
        return jsonify(result)
      else:
        result = Order.query.filter_by(id = id).first()
        result = asdict(result)
        result['order_details'] = OrderDetail.query.filter_by(order_id = id).all()
        return jsonify(result)

    def post(self):
        payment = request.json['payment']
        machine_id = request.json['machine_id']
        net_price = request.json['net_price']
        order_details = request.json['order_details']
        new_Order = Order(payment=payment, net_price=net_price,
                          machine_id=machine_id)
        # print(order_details)
        db.session.add(new_Order)
        db.session.commit()
        new_order_details = []
        for detail in order_details:
            new_order_details.append(OrderDetail(
                order_id=new_Order.id, product_id=detail['product_id'], quantity=detail['quantity']))
        db.session.add_all(new_order_details)
        db.session.add(new_Order)
        db.session.commit()

        return jsonify(new_Order)
