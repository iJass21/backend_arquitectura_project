# api/repositories/user_repository.py
from api.models import User

class UserRepository:
    @staticmethod
    def find_all():
        return User.objects.all()

    @staticmethod
    def create(user_data):
        return User.objects.create(**user_data)

    @staticmethod
    def update(user_id, user_data):
        user = User.objects.get(id=user_id)
        for key, value in user_data.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def delete(user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        return True

    @staticmethod
    def find_by_email(email):
        return User.objects.filter(email=email).first()

    @staticmethod
    def find_by_id(user_id):
        return User.objects.get(id=user_id)
