from django.db import models

# Create your models here.


class Teams(models.Model):
    Team_Id = models.IntegerField(primary_key=True)
    Team_Name = models.CharField(max_length=200)
    Team_Stadium = models.CharField(max_length=500)
    Team_Location = models.CharField(max_length=500)

class Fixture(models.Model):
    Fixture_Id = models.IntegerField(primary_key=True)
    Fixture_Home_Team = models.IntegerField()
    Fixture_Away_Team = models.IntegerField()
    Fixture_Date = models.DateTimeField()


