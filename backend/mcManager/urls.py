from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('servers', views.serversView),
    path('jars', views.jarsView),
]
