
from django.urls import path
from . import views

urlpatterns = [
    path(r'demande', views.post_list, name='form'),
    path(r'',views.accueil_view, name='accueil' )
]
