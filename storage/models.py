from django.db import models

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    email = models.EmailField()
    Name = models.CharField(max_length=200, default='N/A')

# Contact model field to collect user contact email, name, and note
class Contact(models.Model):
    Name = models.CharField(max_length=200)
    note = models.TextField()
    email = models.EmailField()

class Room(models.Model):
    Name = models.CharField(max_length=200)
    FloorNumber = models.IntegerField()
    RoomNumber = models.IntegerField()

class CyberSkill(models.Model):
    Name = models.CharField(max_length=200)

class DevSkill(models.Model):
    Name = models.CharField(max_length=200)

class CloudPlatform(models.Model):
    Name = models.CharField(max_length=200)