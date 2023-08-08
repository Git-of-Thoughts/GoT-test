import firebase_admin
from firebase_admin import auth, db

class FirebaseService:
    def __init__(self):
        self.app = firebase_admin.initialize_app()

    def authenticate_user(self, email, password):
        try:
            user = auth.get_user_by_email(email)
            if user:
                return user
        except:
            return None

    def create_user(self, email, password):
        try:
            user = auth.create_user(
                email=email,
                password=password,
            )
            return user
        except:
            return None
