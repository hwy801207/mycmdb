from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = None  
        try:
            user = self.model(username = username, email = self.normalize_email(email))
            user.set_password(password)
            user.save(using=self._db)
        except Exception as err:
            print(err.message)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)

    objects = UserManager()

    USERNAME_FIELD= 'username'
    REQUIRED_FIELD=['email', 'username']

