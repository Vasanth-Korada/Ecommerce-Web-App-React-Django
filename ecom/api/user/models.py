from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length = 50, default = "Anonymous User")
    first_name = models.CharField(max_length = 50, default = "")
    last_name = models.CharField(max_length = 50, default = "")
    email = models.EmailField(max_length = 250, unique = True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length = 20, blank = True, null = True)
    gender = models.CharField(max_length = 10, blank = True, null = True)

    session_token = models.CharField(max_length = 250, default = "0")

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
