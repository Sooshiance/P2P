from rest_framework import exceptions

from .models import User, OTP


class UserRepository:
    @staticmethod
    def create_user(**kwargs) -> User:
        return User.objects.create_user(**kwargs)

    @staticmethod
    def get_user_by_username(username) -> User:
        try:
            return User.objects.get(username=username)
        except exceptions.NotFound as e:
            raise exceptions.ValidationError(str(e))

    @staticmethod
    def get_user_by_id(user_id) -> User:
        return User.objects.get(pk=user_id)


class OTPRepository:
    @staticmethod
    def create_otp(user: User, otp: str) -> OTP:
        return OTP.objects.create(user=user, otp=otp)

    @staticmethod
    def get_otp(user: User, otp: str):
        return OTP.objects.filter(user=user, otp=otp).first()
