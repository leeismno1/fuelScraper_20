from flask import Flask, render_template
from fuel_scraper_june20 import create_fuel_table
from fuel_scraper_june20 import fuel_table_data
from fuel_scraper_june20 import PREMIUM_UNLEADED, NORTH_OF_RIVER, TOMORROW, TODAY, YESTERDAY

app = Flask(__name__)

@app.route('/')
def index():
    fuel_data = fuel_table_data(PREMIUM_UNLEADED, NORTH_OF_RIVER, TOMORROW)
    list_fuel = create_fuel_table(fuel_data)
    return list_fuel

"""@app.route('/Hello/')
def index():
    return 'Hello world'

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
