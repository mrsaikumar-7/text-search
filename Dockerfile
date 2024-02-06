# Use the official Python image as a base image
FROM python:3.8

# Install dockerize
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.6.1.tar.gz \
    && rm dockerize-linux-amd64-v0.6.1.tar.gz

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code to the container
COPY . /app/

# Expose the port that the application will run on
EXPOSE 8000

# Command to run the application using dockerize
CMD ["dockerize", "-wait", "tcp://db:5432", "-timeout", "20s", "python", "manage.py", "runserver", "0.0.0.0:8000"]
