from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models


class UserManager(DjangoUserManager):
    def create_facebook_user(self, user_info):
        return self.create_user(
            username=user_info['id'],
            first_name=user_info.get('first_name', ''),
            last_name=user_info.get('last_name', ''),
            user_type=User.USER_TYPE_FACEBOOK
        )


class User(AbstractUser):
    USER_TYPE_DJANGO = 'django'
    USER_TYPE_FACEBOOK = 'facebook'
    CHOICES_USER_TYPE = (
        (USER_TYPE_DJANGO, 'Django'),
        (USER_TYPE_FACEBOOK, 'Facebook'),
    )
    user_type = models.CharField(max_length=20, choices=CHOICES_USER_TYPE, default=USER_TYPE_DJANGO)

    objects = UserManager()