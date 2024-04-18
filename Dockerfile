# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the app directory contents into the container at /app
COPY . /app

# Copy scripts into the container
COPY scripts /app/scripts

# Install any needed packages specified in requirements.txt
# Assume requirements.txt is in the app folder; adjust if located elsewhere
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Envs
ENV PINECONE_API_KEY '452a8f55-60c0-4f38-8cc8-7b24a7d4e3cd'
ENV HF_API_KEY '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'

# Define environment variable
ENV FLASK_APP app/app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Run the application
CMD ["flask", "run"]
