# C:\Users\Hp\Desktop\FLASK-LOGIN\login-assignment\app\db\db.py
# from flask import app
from itsdangerous import URLSafeTimedSerializer as Serializer
import mongoengine
from flask_login import UserMixin
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

class User(UserMixin, mongoengine.Document):
    first_name = mongoengine.StringField(required=True)
    last_name = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True, unique=True)
    registration_number = mongoengine.StringField(required=True)
    mobile_number = mongoengine.StringField(required=True)
    address = mongoengine.StringField(required=True)
    password = mongoengine.StringField(required=True)

    meta = {
        'indexes': [
            {'fields': ['registration_number']},
            {'fields' : ['email'], 'unique':True}
        ]
    } 


    def get_reset_token(self, expires_sec=1800):
        # Generate a reset token for password reset
        s = Serializer(SECRET_KEY, expires_sec)
        return s.dumps({'user_id': str(self.id)},  salt='password-reset')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token, salt='password-reset', max_age=1800)
            user_id = data['user_id']
        except:
            return None
        return User.objects(id=ObjectId(user_id)).first()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
