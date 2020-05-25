from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
import misaka


# Create your models here.
User = get_user_model()

register = template.library()


class Group(models.Model):
  pass


class GroupMember(models.Model):
	group = models.ForeignKey(Group, related_name='memberships')
	user = models.ForeignKey(User, related_name='user_group')

  def __str__(self):
    return self.username

  class Meta:
    unique_together = ('group', 'user')
