from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def hello(request):
    return HttpResponse("Hello from Monitoring app!")

def status(request):
    return HttpResponse("Server monitoring is running!")

def health(request):
    return JsonResponse(
        {"status": "healthy",
         "service": "server monitoring"
         })
