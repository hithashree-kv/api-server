# Use the official Python 3.12 slim image as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file first
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining application files
COPY . .

# Expose the port the Flask app listens on
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]