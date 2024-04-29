from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .models import Exhibit, Email
from django.http import HttpResponse
from django.contrib import messages

def html_view(request, pk):
    html_page = get_object_or_404(Exhibit, pk=pk)
    return render(request, 'exhibit_template.html', {'html_page': html_page})

def homepage_view(request):
    html_pages = Exhibit.objects.all()  # Retrieve all HTMLPage objects from the database
    return render(request, 'homepage.html', {'html_pages': html_pages})
def exhibits(request):
    html_pages = Exhibit.objects.all()  # Retrieve all HTMLPage objects from the database
    return render(request, 'exhibits.html', {'html_pages': html_pages})
def play(request):
    return render(request, 'play.html')
def tpa_play(request):
    return render(request, 'tpa_play.html')
def moreinfo(request):
    return render(request, 'moreinfo.html')
def about(request):
    return render(request, 'about.html')
from django.shortcuts import render

def map(request):
    return render(request, 'tpa_play.html', {})
def feedback(request):
    return render(request, 'feedback.html')
def submit_feedback(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        # Create and save the new feedback entry
        Email.objects.create(name=name, email=email)
        messages.success(request, 'Thank you for your feedback!')
        return render(request, 'homepage.html')
    else:
        return HttpResponse('Invalid request', status=400)
    