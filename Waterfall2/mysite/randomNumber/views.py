from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import random

def getRando():
    return random.randint(1,1000000)
def index(request):
    rando = getRando()
    return HttpResponse(str(rando))