from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="mc_index"),
    path("servers/", views.server_list, name="mc_server_list"),
    path("servers/<int:server_id>/", views.server, name="mc_server"),
]
