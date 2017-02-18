from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def result():
    if request.method == 'POST':
        if request.form['money_type'] == 'monthly':
            money_type = "payment per hour"
            calculated = calculate_per_hour(request.form)
        elif request.form['money_type'] == 'hourly':
            money_type = "month salary"
            calculated = calculate_monthly(request.form)
        else:
            return render_template('index.html')
        return render_template("calculate.html", result=(calculated, money_type))


def calculate_per_hour(request_form):
    money_amount = int(request_form['moneyAmount'])
    hours = int(request_form['hours'])
    days = int(request_form['days'])
    calculated = round(money_amount / days / hours, 2)
    return calculated


def calculate_monthly(request_form):
    money_amount = float(request_form['moneyAmount'])
    hours = int(request_form['hours'])
    days = int(request_form['days'])
    calculated = round(money_amount * days * hours, 2)
    return calculated


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', request.path)
    return render_template('404.htm')


if __name__ == '__main__':
    app.run(debug=True)
