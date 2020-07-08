#Posts Models

#Django
from django.db import models


#User Model
class User(models.Model):
    
    email = models.EmailField()
    password = models.CharField(max_length = 100)

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)

    is_admin = models.BooleanField(default = False)

    bio = models.TextField()

    country = models.CharField(
        null = True,
        blank = True,
        max_length = 50
        )

    birthdate = models.DateField(blank = True, null = True)

    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    #Return email
    def __str__(self):
        return self.email
