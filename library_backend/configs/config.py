import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # MongoDB
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/library_db')
    
    # Redis для Celery
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    
    # JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-in-production')
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 час
    JWT_REFRESH_TOKEN_EXPIRES = 604800  # 7 дней
    
    # S3 (AWS или MinIO)
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL')  # Для MinIO
    AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME', 'library-books')
    AWS_S3_MAX_FILE_SIZE = 100 * 1024 * 1024  # 100 МБ
    
    # Справочники
    GENRES = [
        "Фантастика", "Детектив", "Романтика", "Приключения", "Фэнтези",
        "Ужасы", "Исторический роман", "Бизнес-литература", 
        "Научно-популярная литература", "Поэзия", "Драма", "Комедия"
    ]
    
    LANGUAGES = ["ru", "en", "de", "fr", "es"]
