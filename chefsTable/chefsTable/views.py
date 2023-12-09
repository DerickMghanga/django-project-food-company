from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("404: Page Not Found")

# custom error displayed at the inspect tools
def lemon(request):
    return HttpResponseNotFound("Little lemon")