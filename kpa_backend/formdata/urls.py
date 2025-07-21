from django.urls import path
from .views import wheel_specifications_view

urlpatterns = [
    path('api/forms/wheel-specifications/', wheel_specifications_view),
]
