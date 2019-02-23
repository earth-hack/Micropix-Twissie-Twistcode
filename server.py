from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os, uuid
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')


@app.route("/image", methods=['POST'])
def uploadImage():
    image = request.files['file']
    file_name = uuid.uuid4().hex
    image.save(os.path.join(app.root_path, 'static/upload', file_name))
    return jsonify(output=file_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='true')