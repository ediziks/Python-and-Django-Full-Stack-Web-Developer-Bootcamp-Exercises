from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import Users


# Create your views here.
def index(req):
  return HttpResponse('<em>My 2nd App</em><p><ul><li><a class="button" href="/admin">Admin</a></li><li><a class="button" href="/help">Help</a></li><li><a class="button" href="/users">Users</a></li></ul></p>')

  
def help(req):
  my_dict = {'get_help': 'Any help needed from appTwo/help.html?'}
  return render(req, 'appTwo/help.html', context=my_dict)
  
def users(req):
  userlist = Users.objects.order_by('first_name')
  my_data = {'show_users': userlist}
  return render(req, 'appTwo/users.html', context=my_data)