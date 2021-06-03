from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@dataclass
class Stock(db.Model):
    id: int
    machine_id: int
    product_id: int
    quantity: int

    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.name