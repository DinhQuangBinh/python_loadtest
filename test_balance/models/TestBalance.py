from django.db import models

class TestBalance(models.Model):
    username = models.CharField(max_length=100)
    password = models.FileField()
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'




