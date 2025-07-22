FROM python:3.12-slim

# Install ffmpeg and other dependencies
RUN apt-get update && apt-get install -y ffmpeg git

# Set work directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
