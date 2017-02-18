from flask import Flask, render_template, request


# moneyAmount = 0
# hours = 0
# days = 0

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        money_amount = int(request.form['moneyAmount'])
        hours = int(request.form['hours'])
        days = int(request.form['days'])
        calculated = round(money_amount / days / hours, 2)
        return render_template("calculate.html", result=calculated)
    elif request.method == 'GET':
        return render_template("calculate.html", result='You are not allowed to go here')


if __name__ == '__main__':
    app.run(debug=True)
