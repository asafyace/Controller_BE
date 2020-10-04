from django.db import models
from django.conf import settings


class Lab(models.Model):
    labname = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.labname


class Server(models.Model):
    Hostname = models.CharField(max_length=120, blank=True)
    IPAddress = models.GenericIPAddressField(blank=True, null=True)
    OS = models.CharField(max_length=32, blank=True)
    lab = models.ForeignKey(Lab, null=True, blank=True,
                            on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    output = models.TextField(blank=True)
    Lastcommand = models.CharField(max_length=120, blank=True)
    runcommand = models.BooleanField(default=False)

    def __str__(self):
        return self.Hostname


class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    os = models.CharField(max_length=32)

    def __str__(self):
        return self.user_name


class Complain(models.Model):
    firstname = models.CharField(max_length=120, blank=True)
    lastname = models.CharField(max_length=120, blank=True)
    subject = models.TextField(blank=True)

    def __str__(self):
        return self.firstname


class Command(models.Model):
    commandname = models.CharField(max_length=220, blank=True)
    os = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.commandname
