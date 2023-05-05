from django.db import models
from django.contrib.auth.models import AbstractUser


class UserNet(AbstractUser):
    id = models.AutoField()
    first_name = models.CharField(max_length=36)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(null=True, blank=True, upload_to="user/avatars/")
    first_login = models.DateTimeField(null=True)
    email = models.EmailField()

