from django.db import models

# Create your models here
class feedback(models.Model):
    name = models.AutoField(primary_key=True)
    person = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)+' '+self.person

class mail(models.Model):
    name = models.AutoField(primary_key=True)
    person = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return str(self.email)
