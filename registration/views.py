from django.shortcuts import render
from django.http import HttpResponseRedirect
import mysql.connector as sql
fn=''
ln=''
em=''
un=''
up=''
g=''
# Create your views here.
def registration(request):
    global fn,ln,em,un,up,g
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="7410",database='newsapp')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                fn=value
            if key=="surname":
                ln=value
            if key=="email":
                em=value
            if key=="usernum":
                un=value    
            if key=="userpassword":
                up=value
            if key=="gender":
                g=value    
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,em,un,up,g)
        cursor.execute(c)
        m.commit()

        return HttpResponseRedirect('/')

        

    return render(request,'registration.html')
