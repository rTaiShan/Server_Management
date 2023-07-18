from django.db import models

class ServerOwner(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=128)

class MinecraftJar(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    version = models.CheckConstraint(max_length=32)
    source = models.CheckConstraint(max_length=128)
    build = models.CheckConstraint(max_length=16)

class MinecraftServer(models.Model):
    owner = models.ForeignKey(ServerOwner, on_delete=models.CASCADE)
    jar = models.ForeignKey(MinecraftJar, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
