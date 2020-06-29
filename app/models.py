from django.db import models

# Create your models here.

class clases(models.Model):
    username=models.CharField(max_length=4)
    age = models.IntegerField()
    fputs = models.IntegerField()

    class Meta:
        db_table="clases"