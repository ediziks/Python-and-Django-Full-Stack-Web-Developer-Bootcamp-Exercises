from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.
# def index(req):
#   return render(req, 'index.html')

# class CBView(View):
#   def get(self, req):
#     return HttpResponse('Class Based Views Here!')

class IndexView(TemplateView):
  template_name = 'index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['injectme'] = 'I am INJECTED!'
    return context