from django.db import models
# from django_cryptography.fields import encrypt
# from django_cryptography.fields import encrypt
# Create your models here.



class Users_data(models.Model):
    username=models.CharField(max_length=25)
    name=models.CharField(max_length=80)
    number = models.CharField(max_length=80)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    # password=encrypt(models.CharField(max_length=10))

    class meta:
        db_tabel="usersapp_users_data"

    def __str__(self):
        return self.name

