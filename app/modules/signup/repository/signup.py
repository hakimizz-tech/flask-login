from typing import Dict
from app.db.db import User

class SignupRepository:
    def insert_user(self, details:Dict[str, any]):
        try:
            user = User(**details)
            user.save()
        except Exception as e:
            print(e)
            return False
        return True

    