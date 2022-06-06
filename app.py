from flask import Flask, render_template, url_for
import getting_api
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    data = getting_api.get_data()
    average = ""
    for athlete in data:
        average = calculate_average(athlete['summary'])
        max_value = calculate_max(athlete['summary'])
        min_value = calculate_min(athlete['summary'])
        athlete['average'] = average
        athlete['max_value'] = max_value
        athlete['min_value'] = min_value
        athlete['count'] = len(athlete['summary'])
        athlete['sum'] = calculate_sum(athlete['summary'])
    return render_template('index.html', data=data)

@app.template_filter('split_date')
def split_date(value):
    time = value.split('.')[0]
    return datetime.strptime(time, '%Y-%m-%dT%H:%M:%S').strftime('%d-%B-%Y')

@app.template_filter('identify_test')
def identify_test(test):
    return test.get('test')

def calculate_average(data):
    total = 0
    for object in data:
        total += object['value']
    return round(total / len(data),2)

def calculate_max(data):
    array_values = []
    for object in data:
        array_values.append(object['value'])
    return max(array_values)

def calculate_min(data):
    array_values = []
    for object in data:
        array_values.append(object['value'])
    return min(array_values)

def calculate_sum(data):
    array_values = []
    for object in data:
        array_values.append(object['value'])
    return sum(array_values)

if __name__ == "__main__":
    app.run(debug=True)

