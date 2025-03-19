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

SSRF (Server-Side Request Forgery) Demonstration

If you were to run this application and then send a request to the /fetch endpoint with a URL that points to an internal service (like http://localhost:5000, http://127.0.0.1, or any other internal IP address), you could potentially demonstrate an SSRF vulnerability. Here's how it works:

    Sending a Request: You would send a POST request to the /fetch endpoint with a JSON body that includes a URL. For example:

json

    {
        "url": "http://localhost:5000/some_internal_endpoint"
    }

    Fetching the URL: The application would then attempt to fetch the content from the specified URL. If the URL points to an internal service that is accessible from the server where the Flask app is running, the request will succeed.

    Response: The application will return the response from the internal service. If the internal service returns sensitive information or allows for further actions (like modifying data), this could lead to security issues.

Example of a Potential SSRF Attack

    Internal Services: If your application is running in an environment where it has access to internal services (like a database admin interface, metadata service, etc.), an attacker could exploit this by sending a request to the /fetch endpoint with a URL that targets those services.

    Sensitive Data Exposure: If the internal service returns sensitive data (like AWS metadata, database information, etc.), the attacker could gain access to that information through the response from your Flask application.

## Important Note

This setup is for educational purposes only. SSRF vulnerabilities can lead to serious security issues, including unauthorized access to internal services and data leaks. Always ensure that your applications are secure and validate user input to prevent such vulnerabilities.
