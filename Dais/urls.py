from django.urls import path
from Dais import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('modal/', views.modal, name="modal"),
    path('flexbox/', views.flexbox, name="flexbox")
]
