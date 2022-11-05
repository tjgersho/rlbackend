from django.db import models


class Rocket(models.Model):
    mission = models.CharField(max_length=1000)
    launch_date = models.DateTimeField()

    @property
    def currentPos(self):
        if self.position.count() > 0:
            return self.position.all().order_by('created').reverse()[0]
        return None

    @property
    def currentVel(self):
        if self.velocity.count() > 0:
            return self.velocity.all().order_by('created').reverse()[0]
        return None

    @property
    def currentAccel(self):
        if self.acceleration.count() > 0:
            return self.acceleration.all().order_by('created').reverse()[0]
        return None

class Position(models.Model):
    X = models.FloatField(blank=False)
    Y = models.FloatField(blank=False)
    Z = models.FloatField(blank=False)
    created = models.FloatField()
    rocket = models.ForeignKey(Rocket, related_name="position", on_delete=models.PROTECT, null=True, blank=True)

 
class Velocity(models.Model):
    Vx = models.FloatField()
    Vy = models.FloatField()
    Vz = models.FloatField()
    rocket = models.ForeignKey(Rocket, related_name="velocity", on_delete=models.PROTECT, null=True, blank=True)
    created = models.FloatField()

class Acceleration(models.Model):
    Ax = models.FloatField()
    Ay = models.FloatField()
    Az = models.FloatField()
    rocket = models.ForeignKey(Rocket, related_name="acceleration", on_delete=models.PROTECT, null=True, blank=True)
    created = models.FloatField()







