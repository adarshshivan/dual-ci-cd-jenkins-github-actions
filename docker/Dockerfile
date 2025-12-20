# Base image (small, stable, CI-friendly)
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy application code
COPY app/main_wrong.py /app/main.py

# Expose application port
EXPOSE 8000

# Environment variables (can be overridden in CI/CD)
ENV APP_ENV=production
ENV APP_PORT=8000

# Run the application
CMD ["python", "main.py"]
