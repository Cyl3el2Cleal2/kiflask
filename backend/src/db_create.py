from models.product import Product
from models.order import Order
from models.order_detail import OrderDetail
from models.machine import Machine
from models.stock import Stock

from app import db

def create_tables():
  Product.__table__.create(db.engine, checkfirst=True)
  Order.__table__.create(db.engine, checkfirst=True)
  OrderDetail.__table__.create(db.engine, checkfirst=True)
  Machine.__table__.create(db.engine, checkfirst=True)
  Stock.__table__.create(db.engine, checkfirst=True)

if __name__ == '__main__':
  create_tables()