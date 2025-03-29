FROM python:3.11-slim

WORKDIR /app

# Скопируйте только requirements.txt сначала
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Затем скопируйте остальные файлы
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]