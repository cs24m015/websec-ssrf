from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def confidentialRoot():
    return jsonify({'status': 'success', 'data': 'This is confidential information!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)