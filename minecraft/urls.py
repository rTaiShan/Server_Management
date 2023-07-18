from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("servers/", views.server_list, name="server_list"),
    path("servers/<int:server_id>/", views.server, name="server"),
]
