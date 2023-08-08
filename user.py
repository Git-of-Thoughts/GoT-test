from firebase_admin import auth

class User:
    @staticmethod
    def register(form):
        user = auth.create_user(
            email=form['email'],
            password=form['password']
        )
        return user.uid

    @staticmethod
    def login(form):
        user = auth.get_user_by_email(form['email'])
        if user and user.check_password(form['password']):
            return user.uid
        return None
