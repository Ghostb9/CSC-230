from django.urls import path
from csctest import views
from .views import html_view, homepage_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import record_time_spent

urlpatterns = [
    path('record_time_spent/', record_time_spent, name='record_time_spent'),
    path('exhibit/<int:pk>/', html_view, name='html_view'),
    path('', homepage_view, name='homepage_view'),# Set as the root of the app
    path('Account/', views.Account, name='Account'),
    path("login/", views.LoginPageView, name='login'),
    path('get_activities/', views.get_activities, name='get_activities'),
    path("Resources/", views.Resources, name='Resources'),
    path("Play/", views.Play, name='Play'),
    path('admin/', admin.site.urls)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)