from django.shortcuts import render
from django.http import HttpResponse
from .models import Pupil

# Create your views here.
def index(request):
    return HttpResponse('Hello,world. You are at the first index......')

def test(request, id):
    return HttpResponse('This is the test page at age of' + str(5 + id))

def get_outer_template(request):
    message = "How is the outer html?"
    students = [
        'mugabi',
        'kenneth',
        'Jerry'
    ]
    context = {'message': 
               }



def get_inner_template(request):
    message = "How is the outer hyml?"
    return render
         