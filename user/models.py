from django.db import models
from django .contrib.auth.models import User

class CustomUser(User):
    phone_number = models.CharField(max_length=14)
    GENDER = [
        ('MALE', 'MALE'),
        ('FAMALE', 'FAMALE')

    ]

    city = models. CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER, default='MALE')
    photo = models.ImageField(upload_to='user/')

    def __str__(self):
        return self.username
    
