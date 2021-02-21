from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class LoginUser(AbstractUser):
    info_right = models.CharField(max_length=32,default='nobody')
