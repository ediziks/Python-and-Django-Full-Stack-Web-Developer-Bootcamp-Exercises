from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(req):
  # return HttpResponse('Hello World!') // this is before templates
  my_dict = {'insert_me': 'Coming from first_app/index.html'}
  return render(req, 'first_app/index.html', context=my_dict)
