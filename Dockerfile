# Use an official Python image as a base
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirment.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirment.txt

# Copy the application code
COPY . .

# Expose the port the application will run on
EXPOSE 8000

# Run the command to start the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]