from flask import Flask, render_template, request
from fuel_scraper_june20 import create_fuel_table
from fuel_scraper_june20 import fuel_table_data, render_form
from fuel_scraper_june20 import PREMIUM_UNLEADED, NORTH_OF_RIVER, TOMORROW, TODAY, YESTERDAY

app = Flask(__name__)

@app.route('/')
def index():
    day_field = request.args.get('day')
    location_field = request.args.get('location')
    fuel_field = request.args.get('fuel')
    fuel_data = fuel_table_data(fuel_field , location_field, day_field)
    list_fuel = render_form() + create_fuel_table(fuel_data)
    return list_fuel
    

"""@app.route('/Hello/')
def index():
    return 'Hello world'

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

