# Use Python slim image
FROM python:3.12-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /code

# Copy the requirements file
COPY requirements.txt /code/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /code/

# Expose port 8000 and start the server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
