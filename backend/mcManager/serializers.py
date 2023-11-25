from rest_framework import serializers
from .models import MinecraftServer, ServerPreferences, ServerOwner, MinecraftJar

class ServerPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerPreferences
        fields = (
            'id',
            'name',
            'description',
        )

class MinecraftJarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinecraftJar
        fields = (
            'id',
            'name',
            'type',
            'version',
            'source',
            'build',
            'path',
        )

class ServerOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerOwner
        fields = (
            'id',
            'name',
            'username',
        )

class MinecraftServerSerializer(serializers.ModelSerializer):
    # owner = ServerOwnerSerializer()
    # jar = MinecraftJarSerializer()
    # preferences = ServerPreferencesSerializer()

    class Meta:
        model = MinecraftServer
        fields = (
            'id',
            'owner',
            'jar',
            'preferences',
            'name',
            'running',
        )
