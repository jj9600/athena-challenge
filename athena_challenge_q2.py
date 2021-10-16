import pandas as pd
import numpy as np
from flask import Flask

app = Flask(__name__)

@app.route('/')
def return_data():
    df = pd.read_json('application.json')

    income = df.loc['income']
    expense = df.loc['expense']
    frequency = df.loc['frequency']


    total_income = income.dot(frequency)
    total_expenses = expense.dot(frequency)
    raw_surplus = total_income - total_expenses

    data = {'Total Monthly Income': [total_income], 'Total Monthly expenses': [total_expenses], 'Raw Surplus': [raw_surplus]}
    df1 = pd.DataFrame(data)
    df1.index = ['AUD ($)']
    df2 = df1.to_html(header="true", table_id="table")
    return df2


if __name__ == "__main__":
    app.run()