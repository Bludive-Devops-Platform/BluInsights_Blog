# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /usr/src/app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app

# Create a folder for SQLite database and images
RUN mkdir /usr/src/app/database /usr/src/app/images

# Expose port
EXPOSE 5001

# Set environment variable for database URL (relative to container)
ENV DATABASE_URL="sqlite:///./database/blog.db"

# Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5001"]

