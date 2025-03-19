# WEBSEC - SSRF Vulnerability Demonstration

This repository contains a simple demonstration of a Server-Side Request Forgery (SSRF) vulnerability using Flask. The setup includes two services: a main SSRF demonstration app and a secondary service that simulates a sensitive endpoint returning confidential information.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Test the SSRF](#test-the-ssrf)
- [Important Note](#important-note)
- [License](#license)

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

## Important Note

This setup is for educational purposes only. SSRF vulnerabilities can lead to serious security issues, including unauthorized access to internal services and data leaks. Always ensure that your applications are secure and validate user input to prevent such vulnerabilities.
