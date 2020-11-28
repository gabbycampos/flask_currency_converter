from flask import Flask, render_template, session, redirect, request
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)

# secret key for session
app.config['SECRET_KEY'] = 'secret-money'

# forex variables
cr = CurrencyRates()
sym = CurrencyCodes()

# Home Route
@app.route('/')
def home():
    """ Displays Home Page"""
    return render_template('home.html')

# Convert Route
@app.route('/convert', methods=['POST'])
def convert_currency():
    """ Convert currencies from form """
    from_input = request.form['from'].upper()
    to_input = request.form['to'].upper()

    # if amount is not a number
    try:
        amount = float(request.form['amount'])
    except:
        session['msg'] = 'Not a valid amount!'
        return redirect('/error')

    # if one of the currency inputs is incorrect
    try:
        result = cr.convert(from_input, to_input, amount)
    except:
        if sym.get_symbol(from_input) is None:
            session['msg'] = f'Not a valid currency code: {from_input}'
        else:
            session['msg'] = f'Not a valid currency code: {to_input}'
        return redirect('/error')

    symbol = sym.get_symbol(to_input)

    session['result'] = result
    session['symbol'] = symbol

    return redirect('/result')


# Result Route
@app.route('/result')
def get_result():
    """ Display the amount """
    result = session['result']
    formatted_float = "{:.2f}".format(result)
    symbol = session['symbol']

    return render_template('result.html', result=formatted_float, symbol=symbol)

# Error Route
@app.route('/error')
def get_error():
    """ Display error message """
    msg = session['msg']
    return render_template('error.html', msg=msg)