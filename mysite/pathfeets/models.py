from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    token = models.CharField(max_length=1048, unique=True)
    start = models.DateTimeField('when to start')
    stop = models.DateTimeField('when to stop')

    def __str__(self):
        return self.title

class Position(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    timestamp = models.DateTimeField('time at location')
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)

    def __str__(self):
        return "(%f, %f)" % (self.longitude, self.latitude)
