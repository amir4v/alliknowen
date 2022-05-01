from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('iremember/<int:id>', views.iremember, name='iremember'),
]