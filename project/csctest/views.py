from django.shortcuts import render, get_object_or_404
from .models import Exhibit

def html_view(request, pk):
    html_page = get_object_or_404(Exhibit, pk=pk)
    return render(request, 'exhibit_template.html', {'html_page': html_page})

def homepage_view(request):
    html_pages = Exhibit.objects.all()  # Retrieve all HTMLPage objects from the database
    return render(request, 'homepage.html', {'html_pages': html_pages})