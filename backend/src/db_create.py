from models.user import User
from models.product import Product

from app import db

def create_tables():
  User.__table__.create(db.engine, checkfirst=True)
  Product.__table__.create(db.engine, checkfirst=True)

if __name__ == '__main__':
  create_tables()