
from django.http import HttpRequest, HttpResponse ,HttpResponseRedirect
from django.shortcuts import render
import mysql.connector as sql

em=''
up=''

def login(request):
    global em,up
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="7410",database='newsapp')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                up=value
        
        c="select * from  users where email='{}' and user_password='{}'".format(em,up)
        cursor.execute(c)
        t=tuple(cursor.fetchall())

        if t==():
             return render(request,'error.html')
        else:
            return render(request,"homepage.html")

        
        
        

    return render(request,'login.html')
