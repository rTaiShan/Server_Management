from django.contrib import admin
from mcManager.models import MinecraftServer, MinecraftJar, ServerOwner, ServerPreferences

# Register your models here.
admin.site.register(MinecraftServer)
admin.site.register(MinecraftJar)
admin.site.register(ServerOwner)
admin.site.register(ServerPreferences)
