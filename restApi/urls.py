from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendImage/', views.SendImage.as_view(), name="SendImage")
]
