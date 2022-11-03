from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PositionSerializer
from .models import Position

class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows position to be viewed or edited.
    """
    queryset = Position.objects.all().order_by('created')
    serializer_class = PositionSerializer
    # permission_classes = [permissions.IsAuthenticated]


    def post(self, request, format=None):
        serializer = PositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VelocityViewSet(viewsets.ModelViewSet):

    queryset = Position.objects.all().order_by('created')
    serializer_class = PositionSerializer
