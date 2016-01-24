from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomerUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)
        print("create user")
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        print("create super user")
        return user

class CustomerUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomerUserManager()

    def __str__(self):
        return self.email

    # @property
    # def is_superuser(self):
    #     return self.is_admin
    #
    # @property
    # def is_staff(self):
    #     return False
    #
    # @property
    # def is_active(self):
    #     return self.is_active
    #
    # @property
    # def has_perm(self):
    #     return self.is_admin
    #
    # @property
    # def has_module_perms(self):


