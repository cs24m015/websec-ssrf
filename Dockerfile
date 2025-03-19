FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
COPY confidential_service.py confidential_service.py

# Install Flask if it's not in requirements.txt
RUN pip install Flask

# Default command for the SSRF app
CMD ["python", "app.py"]