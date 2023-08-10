from django.db import models

from django.contrib.auth.models import AbstractBaseUser, \
    PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Users must have an email address.')

        # we here normalize to avoid sensitive

        email = self.normalize_email(email).lower()

        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=70)
    # first_name = models.CharField(max_length=70)
    # last_name = models.CharField(max_length=70)

    # Django manage fields.

    date_joined = models.DateTimeField(auto_now_add=True)
    # date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        # return self.first_name
        return self.username

    def get_short_name(self):
        # return self.last_name
        return self.username

    def get_date_joined(self):
        return self.date_joined

    def __str__(self):
        return self.email
