from django.contrib import admin
from . import models


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
  fields = ['release_year', 'title', 'lenght']

  search_fields = ['title', 'release_year']

  list_filter = ['release_year', 'title', 'lenght']

  list_display = ['title', 'release_year', 'lenght']

  list_editable = ['release_year', 'lenght']


admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)
