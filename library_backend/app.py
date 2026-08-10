from flask import Flask
from flask_jwt_extended import JWTManager
from mongoengine import connect
from celery import Celery

from configs.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Инициализация MongoDB
    connect(host=app.config['MONGODB_URI'], alias='default')
    
    # Инициализация JWT
    jwt = JWTManager(app)
    
    # Регистрация маршрутов (будут добавлены позже)
    @app.route('/')
    def index():
        return {"message": "Library Backend API is running", "status": "ok"}
    
    @app.route('/api/health')
    def health_check():
        return {"status": "healthy", "service": "library-backend"}
    
    return app


# Инициализация Celery для фоновых задач
celery_app = Celery(
    'library_tasks',
    broker=Config.REDIS_URL,
    backend=Config.REDIS_URL
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

# Создание экземпляра приложения
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
