from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    category = [
        ('Owner', 'Owner'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
        ('Internship', 'Internship')
    ]

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to='profile/', default='default_user/def_user.jpg')
    desc = models.TextField(max_length=5000, null=True, blank=True)
    contact_no = models.CharField(max_length=10)
    user_category = models.CharField(choices=category, default='Employee', max_length=50)

    def __str__(self):
        return str(
            (
                self.name.first_name, self.name.last_name ,self.name.username
            )
        )

class CompanyCodeModel(models.Model):
    CompanyId = models.CharField(max_length=50)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_pass = models.CharField(max_length=400, default='companyOffice')

    def __str__(self):
        return str(
            (
                self.user_name.username, self.CompanyId
            )
        )

class Mail(models.Model):
    names = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=500)
    subject = models.CharField(max_length=1000)
    text = models.CharField(max_length=5000)
    files = models.FileField(upload_to='pdf/', blank=True, null=True)
    text_time = models.DateField(default=timezone.now)

    def __str__(self):
        return str(
            (
                self.names.username
            )
        )
    
class SaveDatasM(models.Model):
    names = models.ForeignKey(User, on_delete=models.CASCADE)
    savemail_data = models.CharField(max_length=100)
    user_name = models.CharField(max_length=500)
    subject = models.CharField(max_length=1000)
    text = models.CharField(max_length=5000)
    files = models.FileField(upload_to='pdf/', blank=True, null=True)
    text_time = models.DateField(default=timezone.now)

    def __str__(self):
        return str(
            (
                self.names.username
            )
        )

class CategoryGroupModel(models.Model):
    CGM_Image = models.ImageField(upload_to='CGM/', default='default_user/def_user.jpg')
    CGM_Name = models.CharField(max_length=100)
    CGM_Category = models.CharField(max_length=100)
    CGM_Description = models.CharField(max_length=5000, blank=True, null=True, default='Group Chat, Description!')
    CGM_Slogon = models.CharField(max_length=500, default='Welcome To New Group!')
    CGM_Time = models.DateField(default=timezone.now)

    def __str__(self):
        return self.CGM_Name
    
class UserOfCGM(models.Model):
    Steps = [
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    ]

    UOC_connect = models.ForeignKey(CategoryGroupModel, on_delete=models.CASCADE)
    UOC_Id = models.CharField(max_length=100)
    UOC_username = models.CharField(max_length=300)
    UOC_Time = models.DateField(default=timezone.now)
    UOC_Category = models.CharField(choices=Steps, default='Member', max_length=50)

    def __str__(self):
        return self.UOC_username
    
class CGChartModel(models.Model):
    CGC_ChatLink = models.ForeignKey(CategoryGroupModel, on_delete=models.CASCADE)
    CGC_UserName = models.CharField(max_length=300)
    CGC_Text = models.CharField(max_length=7000, blank=True, null=True)
    CGC_Image = models.ImageField(upload_to='Images/', blank=True, null=True)
    CGC_File = models.FileField(upload_to='File/', blank=True, null=True)
    CGC_Video = models.FileField(upload_to='Video/', blank=True, null=True)
    CGC_Time = models.DateField(default=timezone.now)

    def __str__(self):
        return self.CGC_UserName
