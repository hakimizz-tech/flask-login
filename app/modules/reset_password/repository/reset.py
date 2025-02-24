
from app.db.db import User


class ResetRepository:
    def update_user_password(self, user_id: int, new_password: str):
        updated_count = User.objects(id=user_id).update(password=new_password)
        
        # Check if the user was found and updated
        if updated_count > 0:
            user = User.objects(id=user_id).first()
            return user
        else:
            return None
        
    def get_user_by_email(self, email):
        user = User.objects(email=email).first()
        return user