from django.shortcuts import render
from django.http import HttpResponse
import datetime

def get_data(request):
    response = HttpResponse(content=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return response

def dramas_page(request):

    return render(request, 'dramas.html', locals())
