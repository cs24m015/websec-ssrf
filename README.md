# WEBSEC - SSRF Vulnerability Demonstration

This repository contains a simple demonstration of a Server-Side Request Forgery (SSRF) vulnerability using Flask. The setup includes two services: a main SSRF demonstration app and a secondary service that simulates a sensitive endpoint returning confidential information.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Test the SSRF](#test-the-ssrf)
  - [Explanation](#explanation)
- [Important Note](#important-note)

## Prerequisites

- Docker Desktop

Use Docker Compose in the folder with the files:

```
docker-compose up --build
```

### Test the SSRF

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

### Explanation

1. User-Controlled Input
The fetch endpoint accepts a URL from the user via a JSON payload. This means that an attacker can provide any URL they choose, including internal services or resources that the server has access to.

2. Lack of Input Validation
There is no validation or sanitization of the URL input. An attacker can send a request to the fetch endpoint with a URL that points to internal services, such as http://localhost:5001/confidential

3. Potential for Data Exposure
If the attacker can successfully make a request to an internal service, they may be able to access sensitive information. For example, if the attacker sends a request to the confidential endpoint running on port 5001, they could retrieve confidential data that should not be exposed to external users.

## Important Note

This setup is for educational purposes only. SSRF vulnerabilities can lead to serious security issues, including unauthorized access to internal services and data leaks. Always ensure that your applications are secure and validate user input to prevent such vulnerabilities.
