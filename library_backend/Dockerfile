FROM python:3.9-slim

# Установка системных зависимостей для обработки документов
RUN apt-get update && apt-get install -y \
    poppler-utils \
    pandoc \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копирование requirements и установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]
