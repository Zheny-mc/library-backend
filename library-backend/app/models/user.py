from mongoengine import Document, StringField, EmailField, DateTimeField, BooleanField
from datetime import datetime
import bcrypt

class User(Document):
    email = EmailField(required=True, unique=True)
    name = StringField(required=True, max_length=100)
    password_hash = StringField(required=True)
    role = StringField(required=True, choices=['reader', 'admin'], default='reader')
    created_at = DateTimeField(default=datetime.utcnow)
    is_active = BooleanField(default=True)
    
    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    meta = {
        'collection': 'users',
        'indexes': ['email']
    }
