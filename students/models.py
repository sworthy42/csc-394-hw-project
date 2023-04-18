from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name