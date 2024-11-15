from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} | {self.phone_number} | {self.email}"
