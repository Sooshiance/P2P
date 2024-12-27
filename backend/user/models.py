from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
)

from .managers import AllUser


class User(AbstractBaseUser):
    # Users can send phone or email to `username` field
    username = models.TextField(unique=True)
    # If phone was sent, this flag will become `True`
    is_phone = models.BooleanField(default=False)
    # If email was sent, this flag will become `True`
    is_email = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True, null=False)
    is_staff = models.BooleanField(default=False, null=False)
    is_superuser = models.BooleanField(default=False, null=False)

    objects = AllUser()

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "One Time Password"
        verbose_name_plural = "One Time Passwords"
