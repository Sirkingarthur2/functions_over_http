from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse

def hey_you(request, name):
    return HttpResponse(f"Hey, {name}!")


def age_in(request, this, that):
    age = int(this) - int(that)
    return HttpResponse(f"{age}")

def order_total(request, burgers, fries, drinks) -> HttpResponse:
    total = int(burgers) * 4.50 + int(fries) * 1.5 + int(drinks) * 1
    return HttpResponse(f'${total}')