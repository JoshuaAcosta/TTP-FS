from app import db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passphrase = db.Column(db.String(), nullable=False)
    balance = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name