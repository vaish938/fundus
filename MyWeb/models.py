# models.py

from django.db import models

class User(models.Model):
    email = models.EmailField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    tel = models.CharField(blank=True, null=True)
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # Note: This is just for demonstration; use a more secure way to store passwords

    def __str__(self):
        return self.email
    class Meta:
        db_table = 'myweb_user'
