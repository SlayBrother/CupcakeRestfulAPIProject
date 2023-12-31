"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_img = 'https://tinyurl.com/demo-cupcake'

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """The model for our cupcakes"""

    __tablename__ = 'cupcake'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=default_img)