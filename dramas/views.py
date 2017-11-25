from django.shortcuts import render
from django.http import HttpResponse
import datetime
import pymysql

def get_data(request):

    conn = pymysql.connect(host="localhost", user="root", passwd="Fourfive45", db="drama_db")
    myCursor = conn.cursor()
    myCursor.execute("select * from dramas")
    # print(myCursor.fetchall())
    rows = myCursor.fetchall()

#    response = HttpResponse(content=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    response = HttpResponse(content=rows)
    return response

def dramas_page(request):

    return render(request, 'dramas.html', locals())
