from flask import Flask, request, jsonify, render_template_string
import requests
import logging
import socket
import ipaddress
from urllib.parse import urlparse

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# --- Sicherheitsfunktionen für SSRF-Schutz -------------------

def is_public_ip(hostname: str) -> bool:
    try:
        infos = socket.getaddrinfo(hostname, None)
    except socket.gaierror:
        return False  # Host nicht auflösbar

    for info in infos:
        ip_str = info[4][0]
        ip = ipaddress.ip_address(ip_str)
        if ip.is_private or ip.is_loopback or ip.is_link_local \
           or ip.is_multicast or ip.is_reserved:
            return False
    return True

def is_safe_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
    except Exception:
        return False

    if parsed.scheme not in ('http', 'https'):
        return False
    if not parsed.hostname:
        return False
    return is_public_ip(parsed.hostname)

# --- sicherer Endpunkt: /fetch-safe -------------------

@app.route('/fetch-safe', methods=['POST'])
def fetch_safe():
    data = request.get_json(force=True, silent=True) or {}
    url = data.get('url')
    if not url:
        return jsonify({'status': 'error', 'message': 'URL is required'}), 400

    if not is_safe_url(url):
        return jsonify({
            'status': 'error',
            'message': 'URL not allowed (private or invalid)'
        }), 403

    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
    except requests.exceptions.Timeout:
        return jsonify({'status': 'error', 'message': 'Request timed out'}), 408
    except requests.exceptions.RequestException as e:
        return jsonify({
            'status': 'error',
            'message': 'Error fetching the URL',
            'details': str(e)
        }), 500

    return jsonify({'status': 'success', 'data': resp.text}), 200

# --- /fetch (mit SSRF) --------------

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.json.get('url')
    if not url:
        return jsonify({'status': 'error', 'message': 'URL is required'}), 400

    logging.info(f"Fetching URL: {url}")

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        logging.info(f"Successfully fetched data from {url}")
        return jsonify({'status': 'success', 'data': response.text}), 200

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        return jsonify({
            'status': 'error',
            'message': 'HTTP error occurred',
            'details': str(http_err)
        }), 400

    except requests.exceptions.Timeout:
        logging.error("Request timed out")
        return jsonify({'status': 'error', 'message': 'Request timed out'}), 408

    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request exception: {req_err}")
        return jsonify({
            'status': 'error',
            'message': 'An error occurred while fetching the URL',
            'details': str(req_err)
        }), 500

# --- Öffentlicher Endpunkt: /public ---------------------------

@app.route('/public', methods=['GET'])
def publicInformation():
    return jsonify({'status': 'success', 'data': 'This is public information!'})

# --- Web-Oberfläche: Home mit zwei Buttons --------------------

@app.route('/', methods=['GET'])
def index():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>SSRF Demo</title>
          <style>
            body { font-family: sans-serif; padding: 2em; }
            button { margin-right: 1em; padding: 0.5em 1em; }
            pre { background: #f4f4f4; padding: 1em; margin-top: 1em; }
          </style>
        </head>
        <body>
          <h1>SSRF-Demo</h1>
          <button onclick="loadFetch('/fetch')">Unsafe Fetch</button>
          <button onclick="loadFetch('/fetch-safe')">Safe Fetch</button>
          <pre id="result">Klick einen Button, um zu starten…</pre>

          <script>
            async function loadFetch(path) {
              document.getElementById('result').innerText = 'Lade…';
              try {
                const res = await fetch(path, {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ url: 'http://172.20.0.100:5050/public' })
                });
                const json = await res.json();
                document.getElementById('result').innerText =
                  JSON.stringify(json, null, 2);
              } catch (e) {
                document.getElementById('result').innerText = 'Fehler: ' + e;
              }
            }
          </script>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
