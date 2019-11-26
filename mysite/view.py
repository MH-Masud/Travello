from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    bands = [1,2,3,4,5]
    parems = {'name':'masud','place':'BD'}
    message = 'welcome'
    return render(request,'home.html', parems)

def about(request):
    return HttpResponse('this from about')