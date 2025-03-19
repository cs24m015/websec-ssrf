# WEBSEC - SSRF Vulnerability Demonstration

To demonstrate a Server-Side Request Forgery (SSRF) vulnerability, you can create a second service that simulates a sensitive endpoint. This service will return confidential information when accessed. Below, I'll guide you through setting up a simple Flask application that acts as the second service, and then you can modify your existing SSRF demonstration app to access this service.

### Step 1: Create the Second Service

Create a new file called `confidential_service.py`:

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

You can test the SSRF by sending a request to the `/fetch` endpoint with the URL of the confidential service:

```bash
curl -X POST http://localhost:5000/fetch -H "Content-Type: application/json" -d '{"url": "http://localhost:5001/confidential"}'
```

### Step 4: Test the SSRF

When you run the above `curl` command, the SSRF demonstration app will attempt to fetch data from the confidential service. If everything is set up correctly, you should see a response that includes the confidential information:

```json
{
    "status": "success",
    "data": "{\"status\": \"success\", \"data\": \"This is confidential information!\"}"
}
```

### Important Note

This setup is for educational purposes only. SSRF vulnerabilities can lead to serious security issues, including unauthorized access to internal services and data leaks. Always ensure that your applications are secure and validate user input to prevent such vulnerabilities.

make this as README for git

GPT-4o mini:
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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--------------------

User prompt 2 of 2 - 19.3.2025, 19:14:32:
the downloaded readme.txt doesnt look good.. it needs to be github readme style

GPT-4o mini:
Sure! Below is a README formatted in Markdown, which is the standard format for GitHub repositories. You can save this as `README.md` in your project directory.

```markdown
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
- [License](#license)

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Instructions to Save

1. Create a new file named `README.md` in your project directory.
2. Copy and paste the above Markdown content into the `README.md` file.
3. Save the file.

This format will render nicely on GitHub, providing a clear and structured overview of your project.