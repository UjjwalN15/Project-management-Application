from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models import Avg
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .validators import *
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=300, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300, validators=[MinLengthValidator(8), validate_password])
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    date_joined = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return self.email
    
class Projects(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name



ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    ]
class ProjectMembers(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=300, choices=ROLE_CHOICES, default="Member")
    def __str__(self):
        return f'{self.project.name} => {self.user.email}'
    
    
STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]
PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
class Tasks(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=300, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=300, choices=PRIORITY_CHOICES)
    assaigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True) 
    def __str__(self):
        return f'{self.user.email} commented on {self.task.title}'    