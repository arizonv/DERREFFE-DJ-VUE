from django.urls import path
from .views import admin_view, worker_view, client_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('worker/', worker_view, name='worker_view'),
    path('client/', client_view, name='client_view'),
]
