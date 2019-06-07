from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.


def weather(request,city,year):
    print(city)
    print(year)

    return HttpResponse("OK")


def response(request):

    return JsonResponse([{'city':'kk','name':'leon'},{'city':'malacca','name':'jay'}],safe=False,
                        content_type='application/json')