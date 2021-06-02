from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@dataclass
class Machine(db.Model):
    id: int
    name: str
    location: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    location = db.Column(db.Text, unique=True)

    def __repr__(self):
        return '<User %r>' % self.name