FROM python:3.11

# Set the working directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
# Make port 80 available to the world outside this container
EXPOSE 8080
ENTRYPOINT ["ddtrace-run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]