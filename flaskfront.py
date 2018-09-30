
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/netcheck", methods=['POST'])
def netcheck():
    if request.method == 'POST':
        gross = int(request.form['gross_wages'])
        print(gross)

        pre_tax = int(request.form['pretax_ded'])
        print(pre_tax)

        ftc = gross - pre_tax

        payfreq = str(request.form['pay_freq'])
        print(payfreq)

        filing_status = str(request.form['marital_status'])
        print(filing_status)

        output = (status(payfreq, filing_status, ftc))
        print(output)

    return render_template("netcheck.html", variable=output)


if __name__ == '__main__':
    app.debug = True
app.run()