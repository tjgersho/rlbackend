from django.test import TestCase
from datetime import datetime, timedelta

from app.kinematics.calculations import calculateVelocity, calculateAcceleration

# Create your tests here.
from .models import Position, Velocity, Acceleration, Rocket

class AppTestCase(TestCase):

    p1 = None
    p2 = None 
    p3 = None

    v1 = None
    v2 = None
    
    

    def setUp(self):
        # Postition.objects.create(X=1, Y=0, Z=0, created=datetime.datetime(2015, 2, 21, 19, 38, 32, 209148))
        # Postition.objects.create(X=1, Y=0, Z=0, created=datetime.datetime(2015, 2, 21, 19, 38, 32, 209148))
        now =  datetime.now().timestamp()
 
        self.p1 = Position.objects.create(X=0, Y=0, Z=0, created=now)
        self.p2 = Position.objects.create(X=1, Y=1, Z=1, created=now+1000)
        self.p3 = Position.objects.create(X=3, Y=3, Z=3, created=now+2000)


        print("SETUP")

    def teardown(self):
        print("TEARDOWN")

    def test_calcVel(self):
        """Calculate velocity from two position instances"""
        print("Running Test...")


        velocity = calculateVelocity(self.p1, self.p2)
 
        print(velocity.Vx)
        self.assertEqual(velocity.Vx, 1)
        self.assertEqual(velocity.Vy, 1)
        self.assertEqual(velocity.Vz, 1)
  

    def test_calculateAccel(self):
        """Calculate Accel from two velocities instances"""
        print("Running Test...")

        self.v1 = calculateVelocity(self.p1, self.p2)
        self.v2 = calculateVelocity(self.p2, self.p3)

        accel = calculateAcceleration(self.v1, self.v2)

        print(accel)
 
        self.assertEqual(accel.Ax, 1)
        self.assertEqual(accel.Ay, 1)
        self.assertEqual(accel.Az, 1)
