import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proTwo.settings')

import django

django.setup()

import random
from appTwo.models import Users
from faker import Faker

fake = Faker()

def populate(N=5):
  for user in range(N):
    fake_firstname = fake.first_name()
    fake_lastname = fake.last_name()
    fake_mail = fake.ascii_email()

    usr = Users.objects.get_or_create(first_name=fake_firstname, last_name=fake_lastname, mail=fake_mail)

if __name__ == '__main__':
  print('populating script!')
  populate(20)
  print('populating completed!')