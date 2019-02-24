from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from inference import inference
from adaboostapi import testNLP
import os, uuid
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')

@app.route("/image", methods=['POST'])
def uploadImage():
    image = request.files['file']
    file_name = secure_filename(image.filename)
    file_path = os.path.join(app.root_path, 'static/upload', file_name)
    image.save(file_path)
    output = inference(file_path)
    print(output)
    return jsonify(output=output)

@app.route("/nlp", methods=['GET'])
def nlp():
    return render_template('nlp.html')

@app.route("/nlp", methods=['POST'])
def nlp_output():
    output = testNLP()
    return jsonify(output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='true')