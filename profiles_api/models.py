from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """ UserManager for UserProfiles"""
    
    def create_user(self, email, name, password = None):
        """Creating user"""
        if not email:
            raise ValueError("User must have a email")
        
        # normalize email in case of case sensitivity
        email = self.normalize_email(email)
        # create user model object
        user = self.model(email = email, name = name)
        # set password by encryption
        user.set_password(password)
        # save user in DB using specific db 
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password = None):
        """Creating superuser"""
        user = self.create_user(email, name, password)
        # setting flags as true for superuser
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database table User derived from AbstractBaseUser"""

    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name + " with " + self.email

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.name + " with " + self.email

