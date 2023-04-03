from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.role == 'admin'

def is_worker(user):
    return user.role == 'worker'

def is_client(user):
    return user.role == 'client'

admin_required = user_passes_test(lambda user: is_admin(user))
worker_required = user_passes_test(lambda user: is_worker(user))
client_required = user_passes_test(lambda user: is_client(user))

