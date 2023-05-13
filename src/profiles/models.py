from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserNet(AbstractBaseUser):
    id = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=36)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(null=True, blank=True, upload_to="user/avatars/")
    first_login = models.DateTimeField(null=True)
    email = models.EmailField()

