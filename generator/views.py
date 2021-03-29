from django.shortcuts import render
from django.http import HttpResponse
from random import choice as random_choice
from string import punctuation, ascii_uppercase, ascii_lowercase, digits

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    generated_password = ''
    character_set = ascii_lowercase

    if request.GET.get('uppercase'): character_set += ascii_uppercase
    if request.GET.get('numbers'): character_set += digits
    if request.GET.get('special'): character_set += punctuation

    length = int(request.GET.get('length', 16)) # 16 is the default value
    for _ in range(length):
        generated_password += random_choice(character_set)

    return render(request, 'generator/password.html', {'password': generated_password})
