# Start with an official Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy all necessary files from the local machine to the container
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
