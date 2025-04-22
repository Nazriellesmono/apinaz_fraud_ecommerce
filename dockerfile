# Gunakan image Python resmi
FROM python:3.11-slim

# Set work directory di dalam container
WORKDIR /app

# Copy requirements dan install dependency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh kode ke dalam container
COPY ./app /app

# Expose port 8888
EXPOSE 8889

# Jalankan aplikasi dengan uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8889"]