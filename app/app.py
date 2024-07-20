from flask import Flask, jsonify, request

app = Flask(__name__)

# Basic route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Employee Management System"})

# Handle GET request
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)
