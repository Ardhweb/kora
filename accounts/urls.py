from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/', user_login, name="login"),
    path('log-out/', user_logout, name="log_out"),
    path('sign-up/', register, name="sign_up"),
    
]
