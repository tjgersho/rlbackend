from .models import Position, Velocity, Acceleration, Rocket
from rest_framework import serializers


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'X', 'Y', 'Z', 'created']


class VelocitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'X', 'Y', 'Z', 'created']
