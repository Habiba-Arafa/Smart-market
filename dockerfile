# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /myshop

# Copy the requirements file from the host to the container
COPY requirements.txt /myshop/

# Install dependencies listed in the requirements file
RUN pip install --no-cache-dir -r /myshop/requirements.txt

# Copy all project files (including run.py and other files) into the container
COPY myshop /myshop/

# Expose port 5000 for the Flask application
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "/myshop/run.py"]
