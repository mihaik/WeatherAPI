
from flask import Flask, render_template, request
from app import lookup

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/netcheck", methods=['POST'])
def result():
    if request.method == 'POST':
        zip = request.form['zip_code']
        zip = lookup(zip)
        print(zip)

        output = zip
        print(output)

    return render_template("result.html", variable=output[0], variable2=output[1])


if __name__ == '__main__':
    app.debug = True
app.run()
