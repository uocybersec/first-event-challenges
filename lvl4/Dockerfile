# Base image
FROM python:3.8.10-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port on which the application will run
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
