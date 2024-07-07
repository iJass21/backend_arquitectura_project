# api/services/user_service.py
from api.repositories.user_repository import UserRepository
from django.contrib.auth.hashers import make_password

class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.find_all()

    @staticmethod
    def create_user(user_data):
        user_data['password'] = make_password(user_data['password'])
        return UserRepository.create(user_data)

    @staticmethod
    def update_user(user_id, user_data):
        if 'password' in user_data:
            user_data['password'] = make_password(user_data['password'])
        return UserRepository.update(user_id, user_data)

    @staticmethod
    def delete_user(user_id):
        return UserRepository.delete(user_id)

    @staticmethod
    def login(credentials):
        user = UserRepository.find_by_email(credentials['email'])
        if user and user.check_password(credentials['password']):
            return user
        return None

    @staticmethod
    def change_password(user_id, new_password):
        user = UserRepository.find_by_id(user_id)
        if user:
            user.password = make_password(new_password)
            user.save()
            return True
        return False
