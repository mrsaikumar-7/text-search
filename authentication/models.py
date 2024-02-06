# myapp/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Custom manager for CustomUser model
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        # Print a message for creating a regular user
        print("Creating", name, " with password:", password)
        
        # Validate email
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        # Print a message for creating a superuser
        print("Creating superuser with password:", password)
        
        # Set default staff and superuser flags
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        # Call create_user method to create superuser
        return self.create_user(email, name, password, **extra_fields)

# CustomUser model, extending AbstractBaseUser and PermissionsMixin
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Custom primary key field
    id = models.AutoField(primary_key=True)
    
    # User details
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True)
    
    # Timestamps
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)

    # User flags
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Custom manager for user model
    objects = CustomUserManager()

    # Fields required for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
