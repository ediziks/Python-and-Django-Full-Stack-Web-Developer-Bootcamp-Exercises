from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(req):
  return HttpResponse('<em>My 2nd App</em><p><ul><li><a class="button" href="/help">Help</a></li></ul></p>')

  
def help(req):
  my_dict = {'get_help': 'Any help needed from appTwo/help.html?'}
  return render(req, 'appTwo/help.html', context=my_dict)
  