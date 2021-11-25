from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route('/foo', methods=['POST'])
def foo():
    data = request.json
    files = request.files
    return jsonify(data)


if __name__ == '__main__':
    app.debug = True
    app.run()

"""
from flask import Flask, jsonify

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Flask-Heroku"


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=False)

"""