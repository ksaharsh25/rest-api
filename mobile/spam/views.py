from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django.http import HttpResponse,Http404
from django.http import JsonResponse
from django.shortcuts import get_object_or_404,render,redirect
# Create your views here.
class mobilelist(generics.ListAPIView,generics.CreateAPIView):
    
    
    queryset=User.objects.all()
    serializer_class=API
    
class mobiledetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=API
 
class Spamlist(generics.ListAPIView,generics.CreateAPIView):
    
    
    queryset=SpamReports.objects.all()
    serializer_class=Spamapi
    
class SpamDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=SpamReports.objects.all()
    serializer_class=Spamapi
        
def numberexist(request, number):
    
    try:
        contact = User.objects.get(Phone_Number=number)
        return JsonResponse({'name': contact.Name})
    except User.DoesNotExist:
        return JsonResponse({'error': 'Contact not found'}, status=404)
    
        
        # list = User.objects.filter(Phone_Number=number).exists()  
         
        
        # return JsonResponse({'list':list})         

def register(request):
    if request.method=="POST":
        name=request.POST['name']
        number=request.POST['number']
        email=request.POST['email']
        password=request.POST['password']
        
        data=User(Name=name,Phone_Number=number,Email_Address=email,password=password)
        data.save()
        return redirect('login')
    return redirect("This is signup page")      
        
        
def login(request):
    
    if request.method== 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user= User.objects.filter(Email_Address=email,password=password)
        print(email)
        print(password)
        if user.exists():
            return redirect("mark_as_spam")
        else:   
            return HttpResponse("404 error!")
           
    return HttpResponse("This is login page")  




def mark_as_spam(request, mobspam):
    
    report = get_object_or_404(SpamReports, mobspam=mobspam)
    if request.method=="POST":
        mobile=request.POST.get('Phone_number')
        if report.mobspam==mobile:
            report.report_count += 1
            report.save()
        return HttpResponse("This is a spam number")
        
    return redirect("This is spam checking page")      

