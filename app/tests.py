from django.test import TestCase
from datetime import datetime, timedelta

from app.kinematics.calculations import calculateVelocity

# Create your tests here.
from .models import Position, Velocity, Acceleration, Rocket

class AppTestCase(TestCase):

    p1 = None
    p2 = None 

    def setUp(self):
        # Postition.objects.create(X=1, Y=0, Z=0, created=datetime.datetime(2015, 2, 21, 19, 38, 32, 209148))
        # Postition.objects.create(X=1, Y=0, Z=0, created=datetime.datetime(2015, 2, 21, 19, 38, 32, 209148))
        ini_time_for_now =  datetime.now().timestamp()

        future_time =  ini_time_for_now + 1000

        self.p1 = Position.objects.create(X=0, Y=0, Z=0, created=ini_time_for_now)
        self.p2 = Position.objects.create(X=1, Y=1, Z=1, created=future_time)

        print("SETUP")

    def teardown(self):
        print("TEARDOWN")

    def test_calculateVelocity(self):
        """Calculate velocity from two position instances"""
        print("RUnniing Test...")


        velocity = calculateVelocity(self.p1, self.p2)

        print(velocity.Vx)
        self.assertEqual(velocity.Vx, 1)
        self.assertEqual(velocity.Vy, 1)
        self.assertEqual(velocity.Vz, 1)
        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')