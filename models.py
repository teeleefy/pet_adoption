"""Models from SQLAlchemy."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwzmNUwi8ZXZ7gvyK-2WvqeUapjQRHC_JeH-u_6qsLZeS-Oi-kJYBinU7Dc-0EkMj9YIo&usqp=CAU"

class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    age = db.Column(db.Integer, nullable=True)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default= photo)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, default = True)
