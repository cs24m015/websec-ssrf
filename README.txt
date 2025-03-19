# SSRF Vulnerability Demonstration

This repository contains a simple demonstration of a Server-Side Request Forgery (SSRF) vulnerability using Flask. The setup includes two services: a main SSRF demonstration app and a secondary service that simulates a sensitive endpoint returning confidential information.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Create the Second Service](#step-1-create-the-second-service)
  - [Step 2: Run the Second Service](#step-2-run-the-second-service)
  - [Step 3: Modify the SSRF Demonstration App](#step-3-modify-the-ssrf-demonstration-app)
  - [Step 4: Test the SSRF](#step-4-test-the-ssrf)
- [Important Note](#important-note)

## Prerequisites

- Python 3.x
- Flask library

You can install Flask using pip:

```bash
pip install Flask
```

## Setup Instructions

### Step 1: Create the Second Service

Create a new file called `confidential_service.py` and add the following code:

```python
# confidential_service.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/confidential', methods=['GET'])
def confidential():
    return jsonify({'status': 'success', 'data': 'This is confidential information!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```

### Step 2: Run the Second Service

Run the second service in a separate terminal:

```bash
python confidential_service.py
```

This service will be accessible at `http://localhost:5001/confidential`.

### Step 3: Modify the SSRF Demonstration App

You can modify your SSRF demonstration app to allow fetching from the second service. For demonstration purposes, you can use a specific URL that points to the confidential service.

### Step 4: Test the SSRF

You can test the SSRF by sending a request to the `/fetch` endpoint with the URL of the confidential service. Use the following `curl` command:

```bash
curl -X POST http://localhost:5000/fetch -H "Content-Type: application/json" -d '{"url": "http://localhost:5001/confidential"}'
```

If everything is set up correctly, you should see a response that includes the confidential information:

```json
{
    "status": "success",
    "data": "{\"status\": \"success\", \"data\": \"This is confidential information!\"}"
}
```

## Important Note

This setup is for educational purposes only. SSRF vulnerabilities can lead to serious security issues, including unauthorized access to internal services and data leaks. Always ensure that your applications are secure and validate user input to prevent such vulnerabilities.