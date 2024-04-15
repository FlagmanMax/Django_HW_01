from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.one, name='one'),
    path('two/', views.two, name='two'),
    path('three/', views.three, name='three'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
]