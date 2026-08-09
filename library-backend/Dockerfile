FROM python:3.14-slim

# Установка системных зависимостей для конвертации файлов
RUN apt-get update && apt-get install -y \
    poppler-utils \
    pandoc \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копирование требований и установка Python-зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Переменная окружения для Flask
ENV FLASK_APP=app/__init__.py
ENV FLASK_ENV=production

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:create_app()"]
