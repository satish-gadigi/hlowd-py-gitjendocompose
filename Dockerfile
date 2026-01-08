FROM python:3.11-slim

WORKDIR /app
COPY . .

# Upgrade pip first
RUN pip install --upgrade pip setuptools wheel

# Install Flask directly from PyPI
RUN pip install --no-cache-dir flask -i https://pypi.org/simple

CMD ["python", "app.py"]
