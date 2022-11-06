from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from .serializers import PositionSerializer, VelocitySerializer, AccelerationSerializer, RocketSerializer
from .models import Position, Velocity, Acceleration, Rocket
from rest_framework.response import Response
from app.kinematics.calculations import calculateVelocity, calculateAcceleration
from datetime import datetime


class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows position to be viewed or edited.
    """
    queryset = Position.objects.all().order_by('id')
    serializer_class = PositionSerializer

    def create(self, request):
        serializer_context = {
            'request': request,
        }
        serializer = PositionSerializer(data=request.data, context=serializer_context)

        newPos = Position(
            X = float(serializer.initial_data["X"]),
            Y =  float(serializer.initial_data["Y"]),
            Z =  float(serializer.initial_data["Z"]),
            created = serializer.initial_data["created"]
        )

        if serializer.is_valid():
            newPosSaved = serializer.save()
            if newPosSaved.rocket.position.count() > 1:
                lastPos = newPosSaved.rocket.position.order_by('-id')[:2][1]
                vel = calculateVelocity(lastPos, newPosSaved)
                vel.save()

            if newPosSaved.rocket.velocity.count() > 1:
                lastVel = newPosSaved.rocket.velocity.order_by('-id')[:2][1]
                accel = calculateAcceleration(lastVel, vel)
                accel.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'], url_path=r'rocket/(?P<rocketId>[^/.]+)')
    def get_rocket_positions(self, request, rocketId):
        rocket = get_object_or_404(Rocket,  pk=rocketId)
        poistions = rocket.position.all().order_by('created')
        serializer = PositionSerializer(poistions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['DELETE'], url_path=r'(?P<rocketId>[^/.]+)/data')
    def delete_rocket_data(self, request, rocketId):
        rocket = get_object_or_404(Rocket,  pk=rocketId)
        poistions = rocket.position.all().delete()
        return Response(serializer.data, status=204)

class VelocityViewSet(viewsets.ModelViewSet):

    queryset = Velocity.objects.all().order_by('created')
    serializer_class = VelocitySerializer

    @action(detail=False, methods=['GET'], url_path=r'rocket/(?P<rocketId>[^/.]+)')
    def get_rocket_velocities(self, request, rocketId):
        rocket = get_object_or_404(Rocket,  pk=rocketId)
        velocities = rocket.velocity.all().order_by('created')
        serializer = VelocitySerializer(velocities, many=True)
        return Response(serializer.data)

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

    @action(detail=False, methods=['GET'], url_path=r'rocket/(?P<rocketId>[^/.]+)')
    def get_rocket_accelerations(self, request, rocketId):
        rocket = get_object_or_404(Rocket,  pk=rocketId)
        accelerations = rocket.acceleration.all().order_by('created')
        serializer = AccelerationSerializer(accelerations, many=True)
        #return JsonResponse(published_serializer.data, safe=False)
        return Response(serializer.data)

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


    @action(detail=False, methods=['DELETE'], url_path=r'(?P<rocketId>[^/.]+)/data')
    def delete_rocket_data(self, request, rocketId):
        rocket = get_object_or_404(Rocket,  pk=rocketId)
        rocket.position.all().delete()
        rocket.velocity.all().delete()
        rocket.acceleration.all().delete()
        return Response(None, status=204)

