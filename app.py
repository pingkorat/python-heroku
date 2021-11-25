from flask import Flask, jsonify
from pyzbar import pyzbar
from PIL import Image
import requests

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


@app.route('/foo', methods=['POST'])
def foo():
    data = request.json
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=False)


"""
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