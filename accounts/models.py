from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''AbstractUser(AbstractBaseUser, PermissionMixin)の全フィールドを継承
    |id|AbstractUser|
    |username|AbstractUser|
    |first_name|AbstractUser|
    |last_name|AbstractUser|
    |email|AbstractUser|
    |is_staff|AbstractUser|
    |is_active|AbstractUser|
    |date_joined|AbstractUser|
    |password|AbstractBaseUser|
    |last_login|AbstractBaseUser|
    |is_superuser|PermissionMixin|
    |groups|PermissionMixin|
    |user_permissions|PermissionMixin|
    '''
    pass