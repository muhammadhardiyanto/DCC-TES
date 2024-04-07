from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Denny web service!"

@app.route('/hello')
def hello():
    return "Hello, bro!"

@app.route('/data')
def data():
    sample_data = {"name": "Denny", "age": 23, "city": "Tangerang Selatan"}
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)