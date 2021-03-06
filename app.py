from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route('/test', methods=['POST'])
def test():
    data = request.json
    #files = request.files
    return jsonify(data)

"""

from pyzbar import pyzbar
from PIL import Image
from flask import jsonify

def qr(request):
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            barcodes = pyzbar.decode(Image.open(image))

            results = []
            for barcode in barcodes:
                results.append({
                    'code': barcode.data.decode("utf-8"),
                    'type': barcode.type,
                    'postion': {
                        'x': barcode.rect.left,
                        'y': barcode.rect.top,
                        'w': barcode.rect.width,
                        'h': barcode.rect.height
                    }
                })

            if results:
                return jsonify({'results': results})
            else:
                return jsonify({'error': 'NO_DETECT'})

    return jsonify({'ok': True})
"""


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
