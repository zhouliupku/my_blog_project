from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('signin/', views.login_page, name='signin'),
]
