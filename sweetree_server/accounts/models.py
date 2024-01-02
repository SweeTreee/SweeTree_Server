from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    box_name = models.CharField(max_length=20, null=False) # need modify
    box_type = models.CharField(max_length=10, default='None')
    social_auth = models.CharField(max_length=2, default='None')
    is_box_public = models.BooleanField(default=False)

    class UserSocialAuth(models.TextChoices):
        NONE = 'NN', 'None'
        KAKAO = 'KK', 'Kakao'
        GOOGLE = 'GG', 'Google'
        NAVER = 'NV', 'Naver'
