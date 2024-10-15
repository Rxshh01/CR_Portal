from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.


class email_auto(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    def __str__(self) :

        return (f"{self.name} | {self.email}")

class TaskZero(models.Model):
    crid = models.CharField(max_length=10)
    names = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    emails = models.CharField(max_length = 200)
    colgName = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    mobileNo = models.CharField(max_length=10)
    dept = models.CharField(max_length = 200)
    whatsappNo = models.CharField(max_length = 10)
    pincode = models.CharField(max_length = 6)
    address = models.CharField(max_length = 200)
    

    def __str__(self):
        return (
            f"{self.username} | "
            f"{self.crid} | "
            f"{self.names} | "
            f"{self.email} |"
            f"{self.emails}"
            # f"{self.colgName} "
            # f"{self.state} "
            # f"{self.mobileNo} "
            # f"{self.whatsappNo} "
            # f"{self.address} "
            # f"{self.pincode} "
            # f"{self.dept}"
        )



class taskOne(models.Model):
    crid = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length = 200)
    link = models.TextField()
    marks = models.CharField(max_length=100)

    def __str__(self):
        return(
        f"{self.crid} "

        )


class taskTwo(models.Model):
    crid = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length = 200)
    link = models.TextField()
    marks = models.CharField(max_length=100)

    def __str__(self):
        return(
        f"{self.username} | {self.crid}"

        )

class taskThree(models.Model):
    crid = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length = 200)
    link = models.TextField()
    marks = models.CharField(max_length=100)

    def __str__(self):
        return(
        f"{self.username} |{self.crid} "

        )


class taskFour(models.Model):
    crid = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length = 200)
    link = models.TextField()
    marks = models.CharField(max_length=100)

    def __str__(self):
        return(
        f"{self.username} |{self.crid} "

        )

class taskFive(models.Model):
    crid = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length = 200)
    link = models.TextField()
    marks = models.CharField(max_length=100)

    def __str__(self):
        return(
        f"{self.username} |{self.crid} "

        )
class taskSix(models.Model):
    crid = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length = 200)
    link = models.TextField()
    marks = models.CharField(max_length=100)

    def __str__(self):
        return(
        f"{self.username} |{self.crid} "

        )


class taskSeven(models.Model):
    crid = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length = 200)
    link = models.TextField()
    marks = models.CharField(max_length=100)

    def __str__(self):
        return(
        f"{self.username} |{self.crid} "

        )

class taskEight(models.Model):
    crid = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length = 200)
    link = models.TextField()
    marks = models.CharField(max_length=100)

    def __str__(self):
        return(
        f"{self.username} |{self.crid} "

        )
