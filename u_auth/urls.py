from u_auth import views
from django.urls import path

urlpatterns = [
    path('login',views.sign_in,name='login'),
    path('',views.dashboard,name='dashboard'),
]