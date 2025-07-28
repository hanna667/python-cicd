from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask app!"

@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}!"

@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.get_json()
    return jsonify({"received": data})

if __name__ == '__main__':
    app.run(debug=True)
