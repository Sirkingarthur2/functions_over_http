from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hey_you(request, name):
    """Responds with a greeting message."""
    return HttpResponse(f"Hey, {name}!")

def age_in(request, end, birthyear):
    """Calculates the age of a user in a given end year."""
    age = end - birthyear
    return HttpResponse(str(age))

def order_total(request, burgers, fries, drinks):
    """Calculates the total cost of an order."""
    total = (burgers * 4.50) + (fries * 1.50) + (drinks * 1.00)
    return HttpResponse(f"{total:.1f}")
