import string

from .models import User

from django.utils.crypto import get_random_string

from celery import shared_task


@shared_task
def create_users(number):
    for i in range(number):
        username = get_random_string(10, string.ascii_letters)
        password = 10000
        code     = 12
        is_staff = True
        email    = 'sadf'
        User.objects.create(username=username, password=password, code=code, is_staff=is_staff, email=email)
        print('{num}----------user'.format(num=i))
