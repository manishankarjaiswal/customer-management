# Use the official Python image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

# Install required system dependencies
RUN apt-get update && apt-get install -y gcc mariadb-client pkg-config

RUN apt-get update && apt-get install -y python3-dev default-mysql-client default-libmysqlclient-dev build-essential

RUN apt-get install -y wget gnupg2 unzip

RUN apt-get update && apt-get install -y default-jdk

RUN apt-get clean

# Set the working directory
WORKDIR /app

RUN pip install --upgrade pip

# Copy and install Python dependencies
COPY ./requirements.txt .

# Installing dependencies
RUN pip install mysqlclient==2.1.1
RUN pip install gunicorn

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# RUN mv prod.env .env.env
# RUN ["python", "manage.py", "runserver", "0.0.0.0:8000"]