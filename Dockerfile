# Use an official Python runtime as the base image
FROM python:3.10-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install required Python packages
RUN apk add --no-cache --update build-base libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set environment variables
ENV FLASK_APP=flaskr/app.py

# Expose port 5000 for the Flask app to listen on
EXPOSE 5000

# Command to run the app using the flask command
CMD ["flask", "run", "--host=0.0.0.0"]

