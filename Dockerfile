# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Install Tesseract
RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run server.py when the container launches
CMD ["python", "server.py"]

# For poppler
RUN apt-get update && apt-get install -y poppler-utils
