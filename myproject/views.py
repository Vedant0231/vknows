from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def homepage(request):
    return render(request,'homepage.html')
def termsofuse(request):
    return render(request,'termsofuse.html')   
def error(request):
    return render(request,'error.html')      
def about(request):
    return render(request,'about.html')
def feedback(request):
    return render(request,'feedback.html')   
def contact(request):
    return render(request,'contact.html')  
def Entertainment(request):
    return render(request,'Entertainment.html')       
def Political(request):
    return render(request,'Political.html') 
def Farming(request):
    return render(request,'Farming.html')     
def Mythological(request):
    return render(request,'Mythological.html') 
def International(request):
    return render(request,'International.html') 
def Business(request):
    return render(request,'Business.html') 
def Education(request):
    return render(request,'Education.html') 
def Sports(request):
    return render(request,'Sports.html') 
def Medical(request):
    return render(request,'Medical.html') 
