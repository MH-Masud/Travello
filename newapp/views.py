from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return render(request,'index.html')
def add(request):
    
    num1 = int(request.POST['number1'])
    num2 = int(request.POST['number2'])

    result = num1 + num2
    return render(request,'result.html',{'result':result})