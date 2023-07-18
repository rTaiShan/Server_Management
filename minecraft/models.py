from django.db import models

class ServerOwner(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=128)

class MinecraftServer(models.Model):
    owner = models.ForeignKey(ServerOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
