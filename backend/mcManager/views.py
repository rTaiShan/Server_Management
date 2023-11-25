from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MinecraftServerSerializer, MinecraftJarSerializer

from .models import MinecraftJar, MinecraftServer

@api_view(['GET', 'POST'])
def serversView(request : HttpRequest):
    if request.method == 'POST':
        return createServer(request)
    else: # if request.method == 'GET': # default to get
            return getServers(request)    

def getServers(request):
    servers = MinecraftServer.objects.prefetch_related()
    serializer = MinecraftServerSerializer(servers, many=True)
    return Response(serializer.data)

def createServer(request):
    serializer = MinecraftServerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def jarsView(request : HttpRequest):
    if request.method == 'POST':
        return createJar(request)
    else: # if request.method == 'GET': # default to get
            return getJars(request)

def getJars(request):
    jars = MinecraftJar.objects.all()
    serializer = MinecraftJarSerializer(jars, many=True)
    return Response(serializer.data)

def createJar(request):
    serializer = MinecraftJarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
