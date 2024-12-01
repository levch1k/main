from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('register', reg, name='reg'),
    path('auth', login, name='auth'),
    path('logout', logout_view, name='logout'),
    path('make_stat', make_statement, name='make_stat'),
    path('admin_panel', admin_panel, name='admin_panel'),
    path('accept', accept, name='accept'),
    path('deny', deny, name='deny'),
]
