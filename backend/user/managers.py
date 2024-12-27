from django.contrib.auth.models import BaseUserManager


class AllUser(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Need Username")

        user = self.model(
            username=username,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
