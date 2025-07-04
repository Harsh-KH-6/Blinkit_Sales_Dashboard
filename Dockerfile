FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE 8050

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8050", "app:server"] 