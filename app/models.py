from django.db import models


class Rocket(models.Model):
    mission = models.CharField(max_length=1000)
    launch_date = models.DateTimeField()

    @property
    def currentPos(self):
        return self.position.last()



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
    position = models.ForeignKey(Position, related_name="velocity", on_delete=models.PROTECT, null=True, blank=True)
    created = models.FloatField()

class Acceleration(models.Model):
    Ax = models.FloatField()
    Ay = models.FloatField()
    Az = models.FloatField()
    position = models.ForeignKey(Position, related_name="acceleration", on_delete=models.PROTECT, null=True, blank=True)
    created = models.FloatField()







