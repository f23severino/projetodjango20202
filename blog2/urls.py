from django.urls import path
from . import views

app_name = 'avisos'

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
