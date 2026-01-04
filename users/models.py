from django.db import models
from django.contrib.auth.models import AbstractUser,  BaseUserManager
from django.utils.translation import gettext_lazy as __

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):#method for creating normal user
        if not email:
            raise ValueError(__('Email must be set'))
        email = self.normalize_email(email)
        user =self.model(email=email, **extra_fields)#creating a user instance
        user.set_password(password)#hasshing the password
        user.save(using=self._db)#saving user to database
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):#creating superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)#ensuring admin privileges

        if extra_fields.get('is_staff') is not True:
            raise ValueError(__('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(__('Superuser must have is_superuser=True'))
        
        return self.create_user(email,password, **extra_fields)#reusing create_user method (DRY principle)
    
class User(AbstractUser): #custom user model inheriting from AbstractUser
    username = None #removing default username field completely
    email = models.EmailField(unique=True)#email is now the unique identifier
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)#optional
    #additional fields
    name = models.CharField(max_length=50)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, default='user')
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()#attaching custom manager to User model

    def __str__(self):
        return self.email #human readable representation of the user object


