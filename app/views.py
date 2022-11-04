from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets
from rest_framework import permissions
from .serializers import PositionSerializer, VelocitySerializer, AccelerationSerializer, RocketSerializer
from .models import Position, Velocity, Acceleration, Rocket
from rest_framework.response import Response
from app.kinematics.calculations import calculateVelocity
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
            if self.queryset.count() > 0:
                lastPos = self.queryset.last()
                print(lastPos)
                print(serializer.validated_data)
                print(newPos)
                vel = calculateVelocity(lastPos, newPos)
                print(vel.Vx)
                print("--------")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VelocityViewSet(viewsets.ModelViewSet):

    queryset = Velocity.objects.all().order_by('created')
    serializer_class = VelocitySerializer



class AccelerationViewSet(viewsets.ModelViewSet):

    queryset = Acceleration.objects.all().order_by('created')
    serializer_class = AccelerationSerializer


class RocketViewSet(viewsets.ModelViewSet):

    queryset = Rocket.objects.all()
    serializer_class = RocketSerializer

