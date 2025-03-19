# app.py
from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.json.get('url')
    
    if not url:
        return jsonify({'status': 'error', 'message': 'URL is required'}), 400

    # Log the incoming request
    logging.info(f"Fetching URL: {url}")

    try:
        # Make the request to the specified URL
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Log the successful response
        logging.info(f"Successfully fetched data from {url}")

        return jsonify({'status': 'success', 'data': response.text}), 200

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        return jsonify({'status': 'error', 'message': 'HTTP error occurred', 'details': str(http_err)}), 400
    except requests.exceptions.Timeout:
        logging.error("Request timed out")
        return jsonify({'status': 'error', 'message': 'Request timed out'}), 408
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request exception: {req_err}")
        return jsonify({'status': 'error', 'message': 'An error occurred while fetching the URL', 'details': str(req_err)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
