FROM python:3.9-slim-buster

WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY main.py .

# EXPOSE 8000/tcp (порт, который слушает Uvicorn)
EXPOSE 8000/tcp

# Команда запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]