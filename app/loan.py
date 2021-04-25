from collections import defaultdict
import math


def calculate_loan_repayment(loan_amount, annual_interest_rate, loan_period):
    data = defaultdict(dict)
    result = []
    annual_interest_rate = annual_interest_rate/12

    for n in range(loan_period):

        payment_no = n+1

        base1 = 1 + annual_interest_rate
        exponent1 = -loan_period
        payment_amt = (annual_interest_rate * loan_amount) / \
            (1 - math.pow(base1, exponent1))
        payment_amt = round(payment_amt, 2)

        base2 = 1 + annual_interest_rate
        exponent2 = -(1 + loan_period - payment_no)
        principal_amt_paid = payment_amt * math.pow(base2, exponent2)
        principal_amt_paid = round(principal_amt_paid, 2)

        interest_amt_paid = (payment_amt) - (principal_amt_paid)
        interest_amt_paid = round(interest_amt_paid, 2)

        loan_out_bal = (interest_amt_paid/annual_interest_rate) - \
            (principal_amt_paid)
        loan_out_bal = round(loan_out_bal, 2)

        list_of_data = []
        list_of_data.append(payment_no)
        list_of_data.append(payment_amt)
        list_of_data.append(principal_amt_paid)
        list_of_data.append(interest_amt_paid)
        list_of_data.append(loan_out_bal)

        data[n] = list_of_data

        # Initialize matrix
        matrix = []

        # For user input
        for i in data:          # A for loop for row entries
            a = []
            for j in data.get(i):      # A for loop for column entries
                a.append(j)
            matrix.append(a)
        result = matrix

    return result
