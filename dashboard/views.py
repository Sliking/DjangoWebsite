from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/home.html')

def contact(request):
    return render(request, 'dashboard/basic.html', {'content':['If you would like to contact me just email me', 'miguelpinto25@hotmail.com']})
