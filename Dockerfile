# Use ARM64-compatible Python image for Raspberry Pi
FROM python:3.13-slim

# Create the /home/Chatbot directory in the container
RUN mkdir -p /home/ramukaka

# Move to the directory Twitch-chat-bot
WORKDIR /home/ramukaka

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Create the /home/growattreader/logs directory in the container
RUN mkdir -p logs
VOLUME ["/home/ramukaka/logs"]

# Copy the application files into the container
COPY tasker.py ./tasker.py
COPY file_manager.py ./file_manager.py

# Specify the command to run the application
CMD ["python", "tasker.py"]