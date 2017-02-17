from django.db import models

class University(models.Model):
   name = models.CharField(max_length=1000)

   def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(max_length=100)
    longitude = models.FloatField(max_length=100)

class fraternity(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    nickName = models.CharField(max_length=200)
    chapter = models.CharField(max_length=200)
    subscriptionCode = models.DecimalField(decimal_places=20, max_digits=200)
    tempPass = models.DecimalField(decimal_places=20, max_digits=200)
    guardCode = models.DecimalField(decimal_places=20, max_digits=200)

class UserRegister(models.Model):
    user_type = models.CharField(max_length=200)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Email = models.CharField(max_length=1000)
    password = models.CharField(max_length=200)
    ConfirmPassword = models.CharField(max_length=200)
    phoneNumber = models.IntegerField(max_length=10)
    DOB = models.IntegerField(max_length=10)
    pin = models.IntegerField(max_length=10)


