from flask import Flask, render_template, url_for
import getting_api
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    data = getting_api.get_data()
    return render_template('index.html', data=data)

@app.template_filter('split_date')
def split_date(value):
    time = value.split('.')[0]
    return datetime.strptime(time, '%Y-%m-%dT%H:%M:%S').strftime('%d-%B-%Y')

@app.template_filter('split_time')
def split_time(value):
    return value.split('T')[1].split('.')[0]

if __name__ == "__main__":
    app.run(debug=True)

