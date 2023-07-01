from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('video/<str:video_uuid>/',views.WatchVideo,name='watch')
]