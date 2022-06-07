from django.db import models

# Create your models here.
class Admininfo(models.Model):
    user=models.CharField(max_length=20,primary_key=True)
    passworld = models.CharField(max_length=20)
    email= models.EmailField(max_length=100,unique=True)
    
    class Meta:
        db_table = "Admininfo"
        
class Book(models.Model):
 
    bname =models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    price=models.FloatField(default=200)
    def __str__(self):
        return str(self.id)+","+self.bname
    
class Meta:
	db_table = "Book"