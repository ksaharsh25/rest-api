from django.db import models

# Create your models here.
class User(models.Model):
    
    Phone_Number=models.IntegerField(blank=False,null=False,unique=True)
    Name=models.CharField(max_length=50,blank=False,null=False,unique=True)
    Email_Address=models.EmailField(max_length=50,blank=True,null=True)
    password=models.CharField(max_length=100,null=False)
    # id=models.IntegerField(max_length=50,blank=True,null=False,primary_key=True)
    
    def __str__(self):
        return str(self.Phone_Number)
    
 
class SpamReports(models.Model):
    
    mobspam=models.ForeignKey(User,to_field="Phone_Number",on_delete=models.CASCADE)
    report_count=models.IntegerField(default=0)
    
    
        
    