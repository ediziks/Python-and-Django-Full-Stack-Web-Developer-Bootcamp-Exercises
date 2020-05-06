from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import Users
from . import forms


# Create your views here.
def index(req):
  return HttpResponse('<em>My 2nd App</em><p><ul><li><a class="button" href="/admin">Admin</a></li><li><a class="button" href="/help">Help</a></li><li><a class="button" href="/users">Users</a></li></ul></p>')
  
def help(req):
  my_dict = {'get_help': 'Any help needed from appTwo/help.html?'}
  return render(req, 'appTwo/help.html', context=my_dict)

def users(req):
  form = forms.User()

  if req.method == 'POST':
    form = forms.User(req.POST)
    if form.is_valid():
      print('VALIDATION SUCCESSFUL!')
      print('NAME: '+ form.cleaned_data['name'])
      print('EMAIL: '+ form.cleaned_data['email'])

  return render(req, 'appTwo/users.html', {'form': form})