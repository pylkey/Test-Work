# Use python official image from docker hub
FROM python:3.10.13-bullseye


# prevents pyc files from being copied to the container
ENV PYTHONDONTWRITEBYTECODE 1

# Ensures that python output is logged in the container's terminal
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Copy the file 'requirements.txt' from the local build context to the container's file system.
COPY ./req.txt ./req.txt 
# Install python dependencies
RUN pip install -r /req.txt --no-cache-dir


# Set the working directory
WORKDIR /app

# Run Uvicorn to start your Python web application
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8080"]