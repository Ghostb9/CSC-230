from django.urls import path
from . import views
from .views import custom_logout
from .views import CustomLoginView
from .views import account_view

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', custom_logout, name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('add_child/', views.add_child, name='add_child'),
    path('account/', account_view, name='account'),
    path('chatbot-api', views.chatbot_api, name='chatbot_api')

]