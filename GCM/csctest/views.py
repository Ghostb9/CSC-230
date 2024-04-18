from django.shortcuts import render, get_object_or_404
from .models import Exhibit
from .models import TypeofPlay, Activity
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse


def html_view(request, pk):
    html_page = get_object_or_404(Exhibit, pk=pk)
    return render(request, 'exhibit_template.html', {'html_page': html_page})


def homepage_view(request):
    html_pages = Exhibit.objects.all()  # Retrieve all HTMLPage objects from the database
    return render(request, 'homepage.html', {'html_pages': html_pages})


def Account(request):
    return render(request, "Account.html", {})


def LoginPageView(request):
    return render(request, "login.html", {})


def Resources(request):
    return render(request, "Resources.html", {})


def Play(request):
    return render(request, "Play.html", {})


@csrf_exempt
@require_http_methods(["POST"])
def get_activities(request):
    try:
        play_type_name = request.POST.get('play_type')
        type_of_play = TypeofPlay.objects.get(TypeName=play_type_name)
        activities = Activity.objects.filter(category=type_of_play).values('activityName', 'description')

        activities_list = [{'activityName': activity['activityName'], 'description': activity['description']} for
                           activity in activities]

        return JsonResponse({
            'typeDescription': type_of_play.description,
            'activities': activities_list
        })

    except TypeofPlay.DoesNotExist:
        return JsonResponse({'error': 'Play type not found'}, status=404)
