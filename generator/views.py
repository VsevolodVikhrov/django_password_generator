from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, "generator/home.html")


def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    special_characters = list("!@#$%^&*()_-+=<>/?")
    is_uppercase = request.GET.get("uppercase")
    is_numbers = request.GET.get("numbers")
    is_special_characters = request.GET.get("special")
    length = int(request.GET.get("length", 12))
    if is_uppercase:
        characters.extend(uppercase_letters)
    if is_numbers:
        characters.extend(numbers)
    if is_special_characters:
        characters.extend(special_characters)
    the_password = ""
    for i in range(length):
        the_password += random.choice(characters)
    return render(request, "generator/password.html", {"password": the_password})


def developer(request):
    return render(request, "generator/developer.html")