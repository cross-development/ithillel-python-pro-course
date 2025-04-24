FROM python:3.11-slim

WORKDIR /app

# Install dependencies and copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install a package for auto restart
RUN pip install watchdog watchdog[watchmedo] python-dotenv

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run server with auto restart
CMD ["watchmedo", "auto-restart", "--directory=./", "--pattern=*.py", "--recursive", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]