from .models import Position, Velocity, Acceleration, Rocket
from rest_framework import serializers
from datetime import datetime

class VelocitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Velocity
        fields = ['id', 'Vx', 'Vy', 'Vz', 'created']


class AccelerationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Acceleration
        fields = ['id', 'Ax', 'Ay', 'Az', 'created']

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    velocity = VelocitySerializer(required=False, many=True, read_only=True)
    acceleration = AccelerationSerializer(required=False, many=True, read_only=True)
    class Meta:
        model = Position
        fields = ['id', 'X', 'Y', 'Z', 'created', 'acceleration', 'velocity', 'rocket']

    def create(self, validated_data):
        validated_data["created"] = datetime.now().timestamp()
        newpos = Position(**validated_data)
        newpos.save()
        return newpos






class RocketSerializer(serializers.HyperlinkedModelSerializer):
    currentPos = PositionSerializer(required=False, many=True, read_only=True)
    class Meta:
        model = Rocket
        fields = ['id', 'mission', 'launch_date', 'currentPos']