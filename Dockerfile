# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements/base.txt /app

RUN apt -y update && apt install -y libpq-dev python3-dev
RUN apt -y install gcc

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements/base.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Set the FLASK_APP environment variable to the name of the main Flask application file
ENV FLASK_APP=main.py

# Set the default Flask environment to "production"
ENV FLASK_DEBUG=True

# Expose port 5000 for the Flask app to listen on
EXPOSE 5000

RUN flask db migrate && flask db upgrade

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
