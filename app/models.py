from django.db import models


class Rocket(models.Model):
    mission = models.CharField(max_length=1000)

class Acceleration(models.Model):
    Ax = models.FloatField()
    Ay = models.FloatField()
    Az = models.FloatField()
    created = models.DateTimeField()

class Velocity(models.Model):
    Vx = models.FloatField()
    Vy = models.FloatField()
    Vz = models.FloatField()
    created = models.DateTimeField()

class Position(models.Model):
    X = models.FloatField(blank=False)
    Y = models.FloatField(blank=False)
    Z = models.FloatField(blank=False)
    created = models.DateTimeField(blank=False)
    vel = models.OneToOneField( Velocity, on_delete=models.CASCADE, null=True, blank=True)
    accel = models.OneToOneField( Acceleration, on_delete=models.CASCADE, null=True, blank=True)
    rocket = models.ForeignKey(Rocket, on_delete=models.PROTECT, null=True, blank=True)





