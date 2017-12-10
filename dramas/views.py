from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import datetime
import pymysql

def get_data(request):

    conn = pymysql.connect(host="127.0.0.1", user="root", passwd="test", db="drama_db")
    myCursor = conn.cursor()
    myCursor.execute("select * from dramas")
    # print(myCursor.fetchall())
    rows = myCursor.fetchall()

#    response = HttpResponse(content=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    response = JsonResponse({'rows': rows})
    return response

def dramas_page(request):

    return render(request, 'index.html', locals())
