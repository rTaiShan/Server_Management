from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=32)
    player_id = models.CharField(max_length=64)

class ServerOwner(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.username} | {self.name}"
    
class MinecraftJar(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    version = models.CharField(max_length=32)
    source = models.CharField(max_length=128)
    build = models.CharField(max_length=16)
    path = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} | {self.type} - {self.source} | {self.version} {self.build}"

class ServerPreferences(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

class MinecraftServer(models.Model):
    owner = models.ForeignKey(ServerOwner, on_delete=models.CASCADE)
    jar = models.ForeignKey(MinecraftJar, on_delete=models.CASCADE)
    preferences = models.ForeignKey(ServerPreferences, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    running = models.BooleanField()

    def __str__(self):
        return f"{self.name} | {self.owner.name}"
