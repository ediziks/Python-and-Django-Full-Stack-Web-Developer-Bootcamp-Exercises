from django.urls import path, re_path
from cbv_app import views


app_name = 'cbv_app'

urlpatterns = [
  path('', views.SchoolListView.as_view(), name='list'),
  re_path(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
  path('create/', views.SchoolCreateView.as_view(), name='create'),
  # pk is same as re_path 2 above
  path('update/<int:pk>', views.SchoolUpdateView.as_view(), name='update'),
  path('delete/<int:pk>', views.SchoolDeleteView.as_view(), name='delete')
]
