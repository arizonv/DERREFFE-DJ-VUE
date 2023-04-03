from django.urls import path
# from .views import LoginAPIView,UserLogout,UserList,Register,UserReport
from .views import user_list

app_name = 'api'

urlpatterns = [
    # AUTH  ######################################################
    # USERS ######################################################
    path('', user_list, name='user_list'),
    # SERVICES ###################################################
    # RESPORT ####################################################
]
