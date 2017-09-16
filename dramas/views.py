from django.shortcuts import render

def dramas(request):


    return render(request, 'dramas.html', locals())