from django.contrib import admin

from .models import MinecraftServer, MinecraftJar, ServerOwner, Player

admin.site.register(MinecraftServer)
admin.site.register(MinecraftJar)
admin.site.register(ServerOwner)
admin.site.register(Player)
