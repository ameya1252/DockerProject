FROM alpine:latest

# Install Python
RUN apk add --no-cache python3 py3-pip

# Create directory structure
RUN mkdir -p /home/data
RUN mkdir -p /home/output  # Ensure this directory is created

# Copy your Python script into the container
COPY script.py /home/script.py

# Set working directory
WORKDIR /home

# Command to run your script
CMD ["python3", "/home/script.py"]
