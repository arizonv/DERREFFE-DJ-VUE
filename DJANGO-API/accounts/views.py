from django.contrib.auth.decorators import login_required
from  api.decorators import admin_required, worker_required, client_required

@login_required
@admin_required
def admin_view(request):
    # Esta vista solo puede ser vista por usuarios autenticados y con el rol 'admin'
    ...

@login_required
@worker_required
def worker_view(request):
    # Esta vista solo puede ser vista por usuarios autenticados y con el rol 'worker'
    ...

@login_required
@client_required
def client_view(request):
    # Esta vista solo puede ser vista por usuarios autenticados y con el rol 'client'
    ...
