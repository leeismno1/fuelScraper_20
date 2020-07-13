from flask import Flask, render_template
# from fuel_scraper_june20 import fuel_table_data

app = Flask(__name__)

@app.route('/')
def index():
    return 'Test'

@app.route('/Hello/')
def index():
    return 'Hello world'

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
