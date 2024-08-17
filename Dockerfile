# Use an NVIDIA CUDA base image
FROM nvidia/cuda:11.6.2-base-ubuntu20.04

# Set up Python
RUN apt-get update && apt-get install -y python3 python3-pip curl
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Ollama
RUN curl https://ollama.ai/install.sh | sh

# Install the required packages
RUN pip3 install --no-cache-dir fastapi uvicorn ollama

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run the application when the container launches
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]