from .models import Position, Velocity, Acceleration, Rocket
from rest_framework import serializers
from datetime import datetime

class VelocitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Velocity
        fields = ['id', 'Vx', 'Vy', 'Vz', 'created', 'rocket']


class AccelerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acceleration
        fields = ['id', 'Ax', 'Ay', 'Az', 'created', 'rocket']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'X', 'Y', 'Z', 'created', 'rocket']

    def create(self, validated_data):
        validated_data["created"] = datetime.now().timestamp()
        newpos = Position(**validated_data)
        newpos.save()
        return newpos

 

class RocketSerializer(serializers.ModelSerializer):
    currentPos = PositionSerializer(required=False, many=False, read_only=True)
    currentVel = VelocitySerializer(required=False, many=False, read_only=True)
    currentAccel = AccelerationSerializer(required=False, many=False, read_only=True)
    class Meta:
        model = Rocket
        fields = ['id', 'mission', 'launch_date', 'currentPos', 'currentVel', 'currentAccel']