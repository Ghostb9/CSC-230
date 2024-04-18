from django.urls import path
from .views import html_view, homepage_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('exhibit/<int:pk>/', html_view, name='html_view'),
    path('', homepage_view, name='homepage_view'),  # Set as the root of the app
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)