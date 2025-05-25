from django.urls import path
from Dais import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('modal/', views.modal, name="modal"),
    path('flexbox/', views.flexbox, name="flexbox"),
    path('d_gray/', views.d_gray, name="d_gray"),
    path('acme_robots/', views.acme_robots, name="acme_robots"),
]
