from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

GENDER_CHOICES=[("MALE","male"),
              ("FEMALE","female")]

class CoreUser(AbstractBaseUser):
    name = models.TextField(max_length = 25)
    username = models.CharField(max_length =25)
    email = models.EmailField()
    profilephoto = models.ImageField(upload_to= 'images')
    birthdate = models.DateField()
    gender = models.ChoiceField(choices = GENDER_CHOICES)


    def __str__(self):
        return self.name

# migrations have not been applied
# perform all migrations
