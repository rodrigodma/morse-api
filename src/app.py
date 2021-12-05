from flask import Flask, render_template, request
from controller.encoding.encoding_controller import EncodingController

app = Flask(__name__)
controller = EncodingController()

@app.route("/", methods = ['POST', 'GET'])
def decode():
    result = 'decode text'
    if request.method == 'POST':
        options = request.form.get('options')
        if options:
            if request.form['options'] == 'decode':
                result = controller.decode(request.form['text'])
            if request.form['options'] == 'encode':
                result = controller.encode(request.form['text'])

    return render_template("index.html", result = result)