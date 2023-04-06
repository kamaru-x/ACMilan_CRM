from django.db import models
from u_auth.models import User

# Create your models here.

class Center(models.Model):
    Reference = models.CharField(max_length=15)
    Name = models.CharField(max_length=50)
    Students = models.IntegerField(default=0)

    def __str__(self):
        return self.Name
    
class Coordinator(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Center1 = models.ForeignKey(Center,on_delete=models.SET_NULL,null=True, related_name='center1')
    Center2 = models.ForeignKey(Center,on_delete=models.SET_NULL,null=True, related_name='center2')
    Number1 = models.CharField(max_length=15,null=True)
    Number2 = models.CharField(max_length=15,null=True)
    Place = models.CharField(max_length=50,null=True)

class Lead(models.Model):
    Reference = models.CharField(max_length=15)
    Student_Name = models.CharField(max_length=50)
    Gardian_Name = models.CharField(max_length=50)
    Contact_Number = models.CharField(max_length=15)
    Location = models.CharField(max_length=50)
    Lead_Mode = models.CharField(max_length=50)
    Lead_Mode_Text = models.CharField(max_length=100,null=True)
    Coordinator = models.ForeignKey(Coordinator,on_delete=models.DO_NOTHING)
    Contact_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Student_Name
    
class Students(models.Model):
    # basic details
    Reference = models.CharField(max_length=15)
    Full_Name = models.CharField(max_length=50)
    Street_Address = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=50,null=True)
    State = models.CharField(max_length=50,null=True)
    Zip_Code = models.CharField(max_length=50,null=True)
    Center = models.ForeignKey(Center,on_delete=models.SET_NULL,null=True)
    # gardian details
    Phone = models.CharField(max_length=15,null=True)
    Email = models.EmailField(null=True)
    Guardian_Name = models.CharField(max_length=50)
    Guardian_Mobile = models.CharField(max_length=15)
    # id proof
    ID_Proof =  models.CharField(max_length=25)
    # other details
    Date_Of_Birth = models.DateField()
    # age group
    Age_Group = models.CharField(max_length=15)
    Preferred_Location = models.CharField(max_length=50,null=True)
    Travel_Mode = models.CharField(max_length=50,null=True)
    Playing_Position = models.CharField(max_length=50)
    # education
    School_Name = models.CharField(max_length=75,null=True)
    School_Address = models.CharField(max_length=100,null=True)
    Study_Standard = models.IntegerField(null=True)
    Study_Devision = models.CharField(max_length=2,null=True)

    def __str__(self):
        return self.Full_Name