from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    subjects = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name
