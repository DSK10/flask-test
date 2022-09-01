from urllib import request
from flask import Flask, request
from mediapipeFaceDetect import Detect
app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    file = request.files['file']
    filename = file.filename
    d = Detect().process(filename)
    return d


if __name__ == "__main__":
    app.run()