from models.user import User
from models.product import Product
from models.order import Order
from models.order_detail import OrderDetail
from models.machine import Machine

from app import db

def create_tables():
  User.__table__.create(db.engine, checkfirst=True)
  Product.__table__.create(db.engine, checkfirst=True)
  Order.__table__.create(db.engine, checkfirst=True)
  OrderDetail.__table__.create(db.engine, checkfirst=True)
  Machine.__table__.create(db.engine, checkfirst=True)

if __name__ == '__main__':
  create_tables()