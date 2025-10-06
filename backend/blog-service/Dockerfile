# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app

# Create folders for database and image storage (used in Kubernetes)
RUN mkdir -p /app/data /app/images

# Environment variables (can be overridden in container runtime)
ENV DB_PATH="/app/data/blog.db"
ENV IMAGE_DIR="/app/images"
ENV IMAGE_BASE_URL="http://localhost:5001/images"
ENV PORT=5001

# Expose app port
EXPOSE 5001

# Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5001"]
 
