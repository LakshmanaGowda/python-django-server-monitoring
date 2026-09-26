from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.utils import timezone


# Create your views here.
def hello(request):
    return HttpResponse("Hello from Monitoring app!")

def status(request):
    return HttpResponse("Server monitoring is running!")

def health(request):
    try:
        connection.ensure_connection()
        database_status = "healthy"
    except Exception:
        database_status = "unhealthy"

    return JsonResponse({
        "status": "healthy",
        "service": "server monitoring",
        "application": "Server Monitoring Application",
        "database": database_status,
        "timestamp": timezone.now().isoformat()
    })
