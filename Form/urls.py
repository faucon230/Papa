
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path(r'home',views.home_view, name='home_view' )
]
