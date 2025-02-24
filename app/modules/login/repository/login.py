from app.db.db import User

class LoginRepository: 
    def get_login_email(self, email):
        user = User.objects(email=email).first() 
        return user  # Return the user object or None if not found
