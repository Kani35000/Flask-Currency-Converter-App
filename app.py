from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import ConversionForm, CryptoForm
from forex_python.converter import CurrencyRates, CurrencyCodes
from valid_form import find_currency_code, isamount
from forex_python.bitcoin import BtcConverter
import secrets

app= Flask(__name__)



# app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['FLASK_ENV']='production'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True 
app.config['SECRET_KEY']='TDjakes35'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
export PATH="$PATH:/usr/local/python3/bin"
# connect_db(app)


@app.route('/', methods=['GET', 'POST'])
def convert():
    """Home Page"""
    form= ConversionForm()
    
    converting_from= form.converting_from.data
    converting_to= form.converting_to.data
    amount= form.amount.data
    
    
    c = CurrencyRates()
    cc = CurrencyCodes()
    
    converting_to_currency_symbol= cc.get_symbol(converting_to)
    
    if request.method == 'POST':
        converting_from=converting_from.upper()
        converting_to=converting_to.upper()
        if find_currency_code(converting_from)!=converting_from and find_currency_code(converting_to)!=converting_to and isamount(amount)== False:
                flash(f"{converting_from} is not a valid currency code", 'danger')                                        
                flash(f"{converting_to} is not a valid currency code", 'danger')
                flash("Amount is not valid", 'danger')
                return redirect('/')
        if find_currency_code(converting_from)!=converting_from and find_currency_code(converting_to)!=converting_to:
                flash(f"{converting_from} is not a valid currency code", 'danger')                                        
                flash(f"{converting_to} is not a valid currency code", 'danger')
                return redirect('/')
        if find_currency_code(converting_to)!=converting_to and isamount(amount)== False:
                flash(f"{converting_to} is not a valid currency code", 'danger')                                        
                flash("Amount is not valid", 'danger')
        if find_currency_code(converting_from)!=converting_from and isamount(amount)== False:
                flash(f"{converting_from} is not a valid currency code", 'danger')                                        
                flash("Amount is not valid", 'danger')
                return redirect('/')
        if find_currency_code(converting_from)!=converting_from:   
            flash(f"{converting_from} is not a valid currency code", 'danger')
            return redirect('/')
        if find_currency_code(converting_to)!=converting_to:           
            flash(f"{converting_to} is not a valid currency code", 'danger')
            return redirect('/')
        if isamount(amount)== False:
            flash("Amount is not valid", 'danger')
        else:
            result= c.convert(converting_from, converting_to, amount)
            return render_template('index.html', form=form, currency_symbol=converting_to_currency_symbol, result=result)

    return render_template('index.html', form=form)
            

# @app.route('/', methods=['GET', 'POST'])
# def todays_market():
#     """This displays todays market via api"""
    

# @app.route('/crypto', methods=['GET', 'POST'])
# def convert_crypto():
#     """convert crypto-currencies"""
#     form= CryptoForm()
    
#     converting_from= form.converting_from.data
#     converting_to= form.converting_to.data
#     amount= form.amount.data
    
    
#     c = CurrencyRates()
#     cc = CurrencyCodes()
    
#     converting_to_currency_symbol= cc.get_symbol(converting_to)
    
#     if request.method == 'POST':
#         converting_from=converting_from.upper()
#         converting_to=converting_to.upper()
#         if find_currency_code(converting_from)!=converting_from and find_currency_code(converting_to)!=converting_to and isamount(amount)== False:
#                 flash(f"{converting_from} is not a valid currency code", 'danger')                                        
#                 flash(f"{converting_to} is not a valid currency code", 'danger')
#                 flash("Amount is not valid", 'danger')
#                 return redirect('/')
#         if find_currency_code(converting_from)!=converting_from and find_currency_code(converting_to)!=converting_to:
#                 flash(f"{converting_from} is not a valid currency code", 'danger')                                        
#                 flash(f"{converting_to} is not a valid currency code", 'danger')
#                 return redirect('/')
#         if find_currency_code(converting_from)!=converting_from:   
#             flash(f"{converting_from} is not a valid currency code", 'danger')
#             return redirect('/')
#         if find_currency_code(converting_to)!=converting_to:           
#             flash(f"{converting_to} is not a valid currency code", 'danger')
#             return redirect('/')
#         if isamount(amount)== False:
#             flash("Amount is not valid", 'danger')
#         else:
#             result= c.convert(converting_from, converting_to, amount)
#             return render_template('index.html', form=form, currency_symbol=converting_to_currency_symbol, result=result)

#     return render_template('index.html', form=form)
            

        
        