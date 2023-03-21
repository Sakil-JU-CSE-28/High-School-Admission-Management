
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from Admission.models import applicant

# Create your views here.
def index(request):
     return HttpResponse("Hello")


