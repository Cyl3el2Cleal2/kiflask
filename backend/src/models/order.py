from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
import datetime

db = SQLAlchemy()

@dataclass
class Order(db.Model):
    __tablename__ = 'order'
    id: int
    machine_id: int
    datetime: DateTime
    payment: float
    net_price: float

    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Float, nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    payment = db.Column(db.Float, nullable=False)
    net_price = db.Column(db.Float, nullable=False)
    # detail = relationship('OrderDetail')

    def __repr__(self):
        return '<User %r>' % self.id