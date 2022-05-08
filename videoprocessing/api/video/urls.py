from django.urls import path
from .views import VideoProcessAPIView

urlpatterns = [
    path('process/', VideoProcessAPIView.as_view(), name='video-process'),
    
]