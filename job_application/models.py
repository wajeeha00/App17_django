from django.db import models

class Form(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    occupation = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} "
    
