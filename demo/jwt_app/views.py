from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def index(request):
    return HttpResponse(json.dumps(request.META['jwt_payload']))