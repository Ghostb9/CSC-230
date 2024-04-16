from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import TypeofPlay, Activity
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "pages/homepage.html", {})


def LoginPageView(request):
    return render(request, "pages/login.html", {})


def Account(request):
    return render(request, "Account.html", {})


def BigJohn(request):
    context = {
        'exhibit_title': 'Big John Exhibit',
        'exhibit_name': 'Big John',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'pages/static/BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'The Glazer Children\'s Museum has expanded its third floor, '
            'which now houses Big John and a new education center for dinosaur-themed '
            'camps and field trips...'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def ArtSmart(request):
    context = {
        'exhibit_title': 'Art Smart Exhibit',
        'exhibit_name': 'Art Smart',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'ChildPlay.png',
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def CentralBank(request):
    context = {
        'exhibit_title': 'CentralBank Exhibit',
        'exhibit_name': 'CentralBank',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'bank.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def Engineer(request):
    context = {
        'exhibit_title': 'Engineer Workshop Exhibit',
        'exhibit_name': 'Engineer Wrokshop',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'e.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def FamilyPlay(request):
    context = {
        'exhibit_title': 'FamilyPlay Exhibit',
        'exhibit_name': 'FamilyPlay',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'Play.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def Farm(request):
    context = {
        'exhibit_title': 'Farm Exhibit',
        'exhibit_name': 'Farm',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def Firehouse(request):
    context = {
        'exhibit_title': 'FireHouse Exhibit',
        'exhibit_name': 'FireHouse',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def Hospital(request):
    context = {
        'exhibit_title': 'Hospital Exhibit',
        'exhibit_name': 'Hospital',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def IceCream(request):
    context = {
        'exhibit_title': 'IceCream Exhibit',
        'exhibit_name': 'Ice Creame',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def KidsPort(request):
    context = {
        'exhibit_title': 'Kidsport Exhibit',
        'exhibit_name': 'Kidsport',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def OceanSandbox(request):
    context = {
        'exhibit_title': 'OceanSandbox Exhibit',
        'exhibit_name': 'Oceansandbox',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def PizzaPlace(request):
    context = {
        'exhibit_title': 'PizzaPlace Exhibit',
        'exhibit_name': 'PizzaPlace',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def PartyPlace(request):
    context = {
        'exhibit_title': 'PartyPlace Exhibit',
        'exhibit_name': 'PartyPlace',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def Publix(request):
    context = {
        'exhibit_title': 'Public Exhibit',
        'exhibit_name': 'Publix',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def Theater(request):
    context = {
        'exhibit_title': 'Theater Exhibit',
        'exhibit_name': 'Theater',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def Forts(request):
    context = {
        'exhibit_title': 'Theater Exhibit',
        'exhibit_name': 'Theater',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def TugBoats(request):
    context = {
        'exhibit_title': 'Tugboats Exhibit',
        'exhibit_name': 'Tugboats',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def Vet(request):
    context = {
        'exhibit_title': 'Vet Exhibit',
        'exhibit_name': 'Vet',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def Waters(request):
    context = {
        'exhibit_title': 'Waters Exhibit',
        'exhibit_name': 'Waters',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def Temp(request):
    context = {
        'exhibit_title': 'Temp Exhibit',
        'exhibit_name': 'Temp',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def FamilyPlayProject(request):
    context = {
        'exhibit_title': 'FPP Exhibit',
        'exhibit_name': 'FPP',
        'text_color': '#4CAF50',
        'background_color': '#6dcff6',
        'exhibit_image': 'BigJohn.png',  # Assuming this image is in your static directory
        'exhibit_text': (
            'Insert Text'
            # ... rest of your text
        )
    }
    return render(request, 'Template.html', context)


def SafetyVillage(request):
    return render(request, "pages/SafetyVillage.html", {})


def Play(request):
    return render(request, "pages/Play.html", {})


def Resources(request):
    return render(request, "pages/Resources.html", {})


@csrf_exempt
@require_http_methods(["POST"])
def get_activities(request):
    try:
        play_type_name = request.POST.get('play_type')
        type_of_play = TypeofPlay.objects.get(TypeName=play_type_name)
        activities = Activity.objects.filter(category=type_of_play).values('activityName', 'description')

        activities_list = [{'activityName': activity['activityName'], 'description': activity['description']} for activity in activities]

        return JsonResponse({
            'typeDescription': type_of_play.description,
            'activities': activities_list
        })

    except TypeofPlay.DoesNotExist:
        return JsonResponse({'error': 'Play type not found'}, status=404)


