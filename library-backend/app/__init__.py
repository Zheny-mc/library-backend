from flask import Flask
from flask_jwt_extended import JWTManager
from mongoengine import connect
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 15))
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES', 30))
    app.config['MAX_CONTENT_LENGTH'] = int(os.getenv('MAX_CONTENT_LENGTH', 104857600))
    
    # MongoDB connection
    mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/library')
    connect(host=mongodb_uri)
    
    # Initialize JWT
    jwt = JWTManager(app)
    
    # Register blueprints
    from app.auth.routes import auth_bp
    from app.books.routes import books_bp
    from app.reader.routes import reader_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(books_bp, url_prefix='/api/books')
    app.register_blueprint(reader_bp, url_prefix='/api/reader')
    
    return app
