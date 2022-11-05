from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets
from rest_framework import permissions
from .serializers import PositionSerializer, VelocitySerializer, AccelerationSerializer, RocketSerializer
from .models import Position, Velocity, Acceleration, Rocket
from rest_framework.response import Response
from app.kinematics.calculations import calculateVelocity, calculateAcceleration
from datetime import datetime


class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows position to be viewed or edited.
    """
    queryset = Position.objects.all().order_by('created')
    serializer_class = PositionSerializer
    # permission_classes = [permissions.IsAuthenticated]


    def create(self, request):
        serializer_context = {
            'request': request,
        }
        serializer = PositionSerializer(data=request.data, context=serializer_context)

        newPos = Position(
            X = float(serializer.initial_data["X"]),
            Y =  float(serializer.initial_data["Y"]),
            Z =  float(serializer.initial_data["Z"]),
            created = datetime.now().timestamp()
        )

        if serializer.is_valid():
            newPosSaved = serializer.save()
            print("ROcket.........")
            print(newPosSaved.rocket.velocity)
            print(newPosSaved.rocket.velocity.count())
            print(newPosSaved.rocket.position.count())
            if newPosSaved.rocket.position.count() > 1:
                lastPos = newPosSaved.rocket.position.order_by('-id')[:2][1]
                vel = calculateVelocity(lastPos, newPosSaved)
                vel.rocket = newPosSaved.rocket
                vel.created = newPos.created
                vel.save()

            if newPosSaved.rocket.velocity.count() > 1:
                lastVel = newPosSaved.rocket.velocity.order_by('-id')[:2][1]
                accel = calculateAcceleration(lastVel, vel)
                accel.rocket = newPosSaved.rocket
                accel.created = newPos.created
                accel.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VelocityViewSet(viewsets.ModelViewSet):

    queryset = Velocity.objects.all().order_by('created')
    serializer_class = VelocitySerializer

    def create(self, request):
        pass
    def update(self, request, pk=None):
        pass
    def partial_update(self, request, pk=None):
        pass
    def destroy(self, request, pk=None):
        pass


class AccelerationViewSet(viewsets.ModelViewSet):

    queryset = Acceleration.objects.all().order_by('created')
    serializer_class = AccelerationSerializer

 

    def create(self, request):
        pass
    def update(self, request, pk=None):
        pass
    def partial_update(self, request, pk=None):
        pass
    def destroy(self, request, pk=None):
        pass


class RocketViewSet(viewsets.ModelViewSet):

    queryset = Rocket.objects.all()
    serializer_class = RocketSerializer

