from flask import Flask, render_template
import fuel_scraper_june20

app = Flask(__name__)

@app.route('/hello/')
def hello():
    return render_template('fuel_report.html')

@app.route('/')
def index():
    return 'Hello world'

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
