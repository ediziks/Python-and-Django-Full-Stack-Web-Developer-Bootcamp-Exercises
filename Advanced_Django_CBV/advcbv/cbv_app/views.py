from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from django.http import HttpResponse
from . import models

# Create your views here.
# def index(req):
#   return render(req, 'index.html')

# class CBView(View):
#   def get(self, req):
#     return HttpResponse('Class Based Views Here!')

class IndexView(TemplateView):
  template_name = 'index.html'

#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['injectme'] = 'I am INJECTED!'
#     return context

class SchoolListView(ListView):
  context_object_name = 'schools'
  model = models.School
  # returns 'school_list'
  # after contex_object_name var, it returns 'schools'

class SchoolDetailView(DetailView):
  context_object_name = 'school_detail'
  model = models.School
  template_name = 'cbv_app/school_detail.html'

class SchoolCreateView(CreateView):
  fields = ('name', 'principal', 'location')
  model = models.School

class SchoolUpdateView(UpdateView):
  fields = ('name', 'principal')
  model = models.School

class SchoolDeleteView(DeleteView):
  model = models.School
  success_url = reverse_lazy('cbv_app:list')