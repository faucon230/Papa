
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path(r'demande',views.demande_view, name='demande_view' )
]
