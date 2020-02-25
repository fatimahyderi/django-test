from django.db import models


# Create your models here.

class Achievments(models.Model):
    photos = models.IntegerField()
    customers = models.IntegerField()
    photographs = models.IntegerField()

    
class Testimonial(models.Model):
    description = models.CharField(max_length=10380)  
    
    def __str__(self):
        return self.description

class Form(models.Model):
    Name = models.CharField(max_length=55)
    Phone_no = models.IntegerField()
    Email = models.CharField(max_length=100)
    Message = models.CharField(max_length=1000)  


    def __str__(self):
        return self.Name