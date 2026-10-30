FROM mcr.microsoft.com/playwright/python:v1.50.0-noble
WORKDIR /worker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY worker ./worker
CMD ["python", "-m", "worker.main"]
