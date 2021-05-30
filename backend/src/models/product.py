from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@dataclass
class Product(db.Model):
    id: int
    name: str
    price: float
    quantity: int

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.name