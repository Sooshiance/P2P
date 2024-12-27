from django.contrib.auth.models import BaseUserManager


class AllUser(BaseUserManager):
    def create_user(
        self, username, email, phone, password=None, first_name=None, last_name=None
    ):
        if not phone:
            raise ValueError("Need Phone")

        if not email:
            raise ValueError("Need Email")

        if not username:
            raise ValueError("Need Username")

        if not first_name:
            raise ValueError("Need Name")

        if not last_name:
            raise ValueError("Need Family Name")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            phone=phone,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, username, email, phone, password, first_name, last_name):
        user = self.create_user(
            phone=phone,
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password, first_name, last_name):
        user = self.create_user(
            phone=phone,
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
