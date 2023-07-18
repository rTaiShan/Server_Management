from django.contrib import admin

from .models import MinecraftServer, ServerOwner

admin.site.register(ServerOwner)
admin.site.register(MinecraftServer)
