#########################
#####
##### URLS FOR ACCOUNTS
#####
#########################


from django.urls import path
from . import views
from .views import custom_logout
from .views import CustomLoginView

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', custom_logout, name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
]