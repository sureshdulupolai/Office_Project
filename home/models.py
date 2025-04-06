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
                self.names.username , self.text_time
            )
        )
    
class SaveMails(models.Model):
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
