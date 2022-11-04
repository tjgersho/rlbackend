from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from app import views

 
router = routers.DefaultRouter()
router.register(r'position', views.PositionViewSet)
router.register(r'velocity', views.VelocityViewSet) 
router.register(r'acceleration', views.AccelerationViewSet) 
router.register(r'rocket', views.RocketViewSet) 


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]