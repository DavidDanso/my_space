from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_picture = models.ImageField(default="avatar-default.gif", null=True, blank=True)
    location = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.user)

class Project(models.Model):
    PRIORITY = (
        ('Low', 'Low'),
        ('Normal', 'Normal'),
        ('High', 'High')
    )
    STATUS = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    )
    title = models.CharField(max_length=200, null=True)
    due_date = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    priority = models.CharField(max_length=200, null=True, choices=PRIORITY)
    contact_name = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Meeting(models.Model):
    title = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=200, null=True)
    time = models.CharField(max_length=200, null=True)
    contact_name = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Deal(models.Model):
    deal_name = models.CharField(max_length=200, null=True)
    amount = models.CharField(max_length=200, null=True)
    currency_name = models.CharField(max_length=200, null=True)
    closing_date = models.CharField(max_length=200, null=True)
    contact_name = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.deal_name




    



