# Library Backend

A Flask-based backend service for a library management system with support for book storage, user authentication, and digital content management.

## Features

- **User Authentication**: JWT-based authentication system
- **Book Management**: CRUD operations for library books
- **Reader Management**: Track reader information and activities
- **File Storage**: S3-compatible storage using MinIO for book files
- **Document Conversion**: Support for PDF, DOCX, and eBook formats
- **Task Queue**: Celery integration with Redis for background tasks

## Tech Stack

- **Backend**: Flask 3.0.0
- **Database**: MongoDB 7.0
- **Authentication**: Flask-JWT-Extended
- **ODM**: MongoEngine
- **Task Queue**: Celery with Redis
- **Storage**: MinIO (S3-compatible)
- **Containerization**: Docker & Docker Compose

## Project Structure

```
workspace/
├── docker-compose.yml      # Main Docker Compose configuration
├── README.md               # This file
└── library-backend/
    ├── app/
    │   ├── __init__.py     # Flask application factory
    │   ├── models/         # Database models
    │   │   └── user.py
    │   └── utils/          # Utility functions
    │       └── enums.py
    ├── Dockerfile          # Backend container configuration
    └── requirements.txt    # Python dependencies
```

## Prerequisites

- Docker and Docker Compose
- Git

## Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd workspace
```

### 2. Start Services with Docker Compose

```bash
docker-compose up -d
```

This will start:
- MongoDB on port 27017
- Redis on port 6379
- MinIO on ports 9000 (API) and 9001 (Console)

### 3. Build and Run the Backend

```bash
cd library-backend
docker build -t library-backend .
docker run -p 5000:5000 --env-file .env library-backend
```

Or use the backend's docker-compose:

```bash
cd library-backend
docker-compose up -d
```

## Configuration

Create a `.env` file in the `library-backend` directory with the following variables:

```env
# Flask Configuration
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret-key
JWT_ACCESS_TOKEN_EXPIRES=15
JWT_REFRESH_TOKEN_EXPIRES=30
MAX_CONTENT_LENGTH=104857600

# MongoDB Connection
MONGODB_URI=mongodb://root:rootpassword@localhost:27017/library?authSource=admin

# MinIO/S3 Configuration
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadminpassword
MINIO_BUCKET=library-books

# Redis Configuration
REDIS_URL=redis://localhost:6379/0
```

## API Endpoints

The API is organized into the following blueprints:

- `/api/auth` - Authentication endpoints (login, register, token refresh)
- `/api/books` - Book management endpoints
- `/api/reader` - Reader management endpoints

## Development

### Local Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r library-backend/requirements.txt
```

3. Set up environment variables (see Configuration section)

4. Run the development server:
```bash
cd library-backend
flask run
```

### Running Tests

```bash
pytest
```

## Docker Services

| Service | Port | Description |
|---------|------|-------------|
| MongoDB | 27017 | NoSQL database |
| Redis | 6379 | Message broker for Celery |
| MinIO API | 9000 | S3-compatible object storage |
| MinIO Console | 9001 | Web UI for MinIO |
| Backend | 5000 | Flask application |

## MinIO Access

- **Console URL**: http://localhost:9001
- **Username**: minioadmin
- **Password**: minioadminpassword
- **Bucket**: library-books (auto-created)

## MongoDB Access

- **Host**: localhost
- **Port**: 27017
- **Username**: root
- **Password**: rootpassword
- **Database**: library

## License

MIT License