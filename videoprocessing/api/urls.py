from django.urls import path, include

urlpatterns = [
    path('video/', include('videoprocessing.api.video.urls')),
    ]