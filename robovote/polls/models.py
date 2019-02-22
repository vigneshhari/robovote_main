from django.db import models

class Team(models.Model):
    Name = models.CharField(max_length = 1000)
    Image = models.CharField(max_length = 10000)
    Bot = models.CharField(max_length = 10000)
    Members = models.CharField(max_length = 1000)
    Desc = models.TextField()
    Backers = models.ManyToManyField('Backer' , null=True, blank=True)
 
    def __str__(self):
        return self.Name

class Backer(models.Model):
    Name = models.CharField(max_length = 1000)
    OId = models.CharField(max_length = 1000)
    LTime = models.DateTimeField()

    def __str__(self):
        return self.Name