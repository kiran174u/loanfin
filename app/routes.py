from app import app
from flask import render_template, request
from app.loan import calculate_loan_repayment


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Loan repayment calculator')


@app.route('/calculate', methods=['POST'])
def calculate():

    loan_amount = float(request.form['loan-amount'])
    annual_interest_rate = float(request.form['interest-rate'])
    loan_period = int(request.form['loan-period'])

    result = calculate_loan_repayment(
        loan_amount=loan_amount, annual_interest_rate=annual_interest_rate, loan_period=loan_period)
    return render_template('/table.html',  title='Loan repayment schedule', result=result)
