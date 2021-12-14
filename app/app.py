"""A simple flask web app"""
from flask import Flask, request, flash
from flask import render_template
from calculator.data_cleaner.dataclean import DataClean
from calculator.calculator import Calculator
from calculator.csv_operations.log_write import LogWrite
from calculator.history.calculation_history import History

app = Flask(__name__)
app.secret_key = 'ayyylmao2021'


@app.route("/")
def index():
    """index  Route Response"""
    return render_template('index.html')


@app.route("/aaatesting", methods=['GET', 'POST'])
def aaatesting():
    return render_template('aaatesting.html')


@app.route("/pylint", methods=['GET', 'POST'])
def pylint():
    return render_template('pylint.html')


@app.route("/principles", methods=['GET', 'POST'])
def principles():
    return render_template('principles.html')


@app.route("/solid", methods=['GET', 'POST'])
def solid():
    return render_template('solid.html')


@app.route("/results", methods=['GET', 'POST'])
def results():
    return render_template('results.html')


@app.route("/calculatorpage", methods=['GET', 'POST'])
def calculatorpage():
    """Post Request Handling"""
    if request.method == 'POST':
        # get the values out of the form
        values = request.form['values']
        operation = request.form['operation']
        # make the tuple
        value_tuple = DataClean.data_process(values)
        if value_tuple == ValueError:
            flash('Invalid Input. Please enter numeric values separated by commas.', 'error')
            return render_template('calculatorpage.html')
        # this will call the correct operation
        getattr(Calculator, operation)(value_tuple)

        # Create a new entry / add results to log
        LogWrite.add_to_log(value_tuple)
        # Write Log
        # Display log
        result = str(History.last_result())

        return render_template('results.html', values=values, operation=operation, result=result)
    # Displays the form because if it isn't a post it is a get request
    else:
        return render_template('calculatorpage.html')
