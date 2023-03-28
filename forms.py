from flask_wtf import FlaskForm
from wtforms import FloatField, StringField
from wtforms.validators import InputRequired, Length


class ConversionForm(FlaskForm):

    converting_from= StringField("Converting From", validators=[InputRequired(), Length(min=3,max=3)])
    converting_to= StringField("Converting To", validators=[InputRequired(), Length(min=3,max=3)])
    amount= FloatField("Amount", validators=[InputRequired()])

class CryptoForm(FlaskForm):

    converting_from= StringField("Converting From", validators=[InputRequired(), Length(min=3,max=3)])
    converting_to= StringField("Converting To", validators=[InputRequired(), Length(min=3,max=3)])
    amount= FloatField("Amount", validators=[InputRequired()])

