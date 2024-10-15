from django.db import models

class fnb_model(models.Model):
    email1 = models.CharField(max_length=400)
    startup_name = models.CharField(max_length=400)
    web_link = models.CharField(max_length=400)
    pvt_yn = models.CharField(max_length=50)
    details = models.CharField(max_length=1000)
    contact = models.IntegerField()
    city = models.CharField(max_length=400)
    theme = models.CharField(max_length=400)
    unique = models.CharField(max_length=1000)
    stage = models.CharField(max_length=400)
    validation = models.CharField(max_length=400)
    patent = models.CharField(max_length=300)
    incubated = models.CharField(max_length=300)
    incubator_name = models.CharField(max_length=400)
    looking_for = models.CharField(max_length=400)

    def __str__(self):
        return self.startup_name

class pitch_submission(models.Model):
    pitch_email = models.CharField(max_length=400)
    pitch_link = models.CharField(max_length=400)
    pitch_video = models.CharField(max_length=400)

    def __str__(self):
        return self.pitch_email
