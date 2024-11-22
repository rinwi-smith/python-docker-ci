# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the app port
EXPOSE 5000

# Command to run the app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
