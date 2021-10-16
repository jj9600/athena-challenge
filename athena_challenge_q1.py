import pandas as pd
import numpy as np


def return_raw_data(path):
    df = pd.read_json(path)
    return df

def show_cumulative_data(path):
    df = return_raw_data(path)

    income = df.loc['income']
    expense = df.loc['expense']
    frequency = df.loc['frequency']

    total_income = income.dot(frequency)
    total_expenses = expense.dot(frequency)
    raw_surplus = total_income - total_expenses

    data = {'Total Monthly Income': [total_income], 'Total Monthly expenses': [total_expenses], 'Raw Surplus': [raw_surplus]}
    df1 = pd.DataFrame(data)
    df1.index = ['AUD ($)']
    print(df1)

if __name__ == "__main__":
    path1='application.json'
    show_cumulative_data(path1)