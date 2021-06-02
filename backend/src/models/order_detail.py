from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@dataclass
class OrderDetail(db.Model):
    __tablename__ = 'order_detail'
    id: int
    order_id: int
    product_id: int
    price: float
    quantity: int

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    # order = relationship('Order')

    def __repr__(self):
        return '<OrderDetail id %r>' % self.id