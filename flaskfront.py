from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/netcheck", methods=['POST'])
def result():
    if request.method == 'POST':
        zip = int(request.form['zip_code'])
        output = zip
    return render_template("result.html", variable=output)


if __name__ == '__main__':
    app.run(debug=True)
