from django.shortcuts import render

# Create your views here.
def index(req):
  return render(req, 'basic_app/index.html')

def other(req):
  return render(req, 'basic_app/other.html')

def relative(req):
  return render(req, 'basic_app/relative_url_templates.html')