# Use the official Python image as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the FastAPI application code into the container
COPY . /app

# Install the required Python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the application runs on
EXPOSE 8881

# Define the command to run your application
CMD ["uvicorn", "mysql:app", "--host", "0.0.0.0", "--port", "8884"]