from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

sample_cupcakes = [
    {
        "flavor": "cherry",
        "size": "large",
        "rating": 5,
        "image": "https://example.com/cherry-cupcake.jpg"
    },
    {
        "flavor": "chocolate",
        "size": "small",
        "rating": 9,
        "image": "https://example.com/chocolate-cupcake.jpg"
    },
]

db.session.add_all(sample_cupcakes)
db.session.commit()