from django.shortcuts import render


# Create your views here.
def index(req):
  my_dict = {'insert_content': 'Hello from first_app'}
  return render(req, 'first_app/index.html', context=my_dict)
