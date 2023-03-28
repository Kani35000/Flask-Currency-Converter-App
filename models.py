from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func



db = SQLAlchemy()



def connect_db(app):
    db.app = app
    db.init_app(app)





# MODELS HERE


class ForexCalc(db.Model):
    __tablename__='forex_calc'

    def __repr__(self):
        """Shows info about user."""
        p =self
        return f"<ForexCalc converting_from={p.converting_from} converting_to={p.converting_to} Amount={p.Amount}>"


    converting_from= db.Column(db.Integer, primary_key=True, autoincrement=True)
    converting_to= db.Column(db.Text, nullable= False, unique=True)
    Amount= db.Column(db.Integer, nullable= False)

    