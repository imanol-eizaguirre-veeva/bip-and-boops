# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file from the host into the container
COPY backend/requirements.txt .
COPY backend/.env .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .
