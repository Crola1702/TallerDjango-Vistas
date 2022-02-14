from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world! Django views")

def crola_view(request):
    return HttpResponse("Hello Crola")

    