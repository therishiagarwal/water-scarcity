# myapp/views.py

from django.shortcuts import render

def groundwater_map(request):
    return render(request, 'groundwater_map.html')
