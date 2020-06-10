# Django imports.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Local imports.
from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, null=False)
    # as phone number can be max 15 digits globally
    # and must have index constraint
    phone_number = models.CharField(max_length=15, db_index=True)
    email = models.EmailField(max_length=75, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # Email & Password are required by default.
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined
    # above should manage objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`
        setting name here as number can be confusing.
        """
        return self.name