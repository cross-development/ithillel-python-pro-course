FROM python:3.11-slim

WORKDIR /app

# Install dependencies and copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8000

