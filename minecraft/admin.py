from django.contrib import admin

from .models import MinecraftServer, MinecraftJar, ServerOwner, Player, ServerPreferences

admin.site.register(MinecraftServer)
admin.site.register(ServerPreferences)
admin.site.register(MinecraftJar)
admin.site.register(ServerOwner)
admin.site.register(Player)
