from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

# By the below steps we are asking for phone number instead of user name even while
# creating a super user

class CustomUser(AbstractUser):

    username = None
    phone_number = models.CharField(max_length = 50 , unique = True)
    email = models.EmailField(unique = True)
    user_bio = models.CharField(max_length = 100)
    user_profile_image = models.ImageField(upload_to = "profile")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()