from django.http import HttpResponse
from .models import UserRegister


def index(request):
    html = ' '

    return HttpResponse(html)

def register(request, userRegister_id):
    return HttpResponse("<h2>This is the user signup page</h2>")
