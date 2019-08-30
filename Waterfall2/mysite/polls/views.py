from django.http import HttpResponse

import random

def getRando():
    return random.randint(1,1000000)
def index(request):
    rando = getRando()
    return HttpResponse(str(rando))