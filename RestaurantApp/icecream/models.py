from django.db import models

# Create your models here.
class icecreams(models.Model):
    ItemNumber=models.IntegerField(primary_key=True)
    IcecreamName=models.CharField(max_length=20,unique=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/',null=True)
    