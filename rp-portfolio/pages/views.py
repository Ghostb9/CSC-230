#########################
#####
##### VIEWS FOR ALL HTML
#####
#########################

#imports functions from django
from django.shortcuts import render
from .models import Post
# imports to handle incoming data about page time spent
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import PageTimeSpent
import json
# views to handle all of said data about page time spent
@require_POST
@login_required
def record_time_spent(request):
    data = json.loads(request.body)
    PageTimeSpent.objects.create(
        user=request.user,
        url=data['url'],
        time_spent=data['time_spent']
    )
    return JsonResponse({"status": "success"})


#functions for showing html sites
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'myapp/post_list.html', {'posts': posts})
def home(request):
    return render(request, "pages/homepage.html", {})
def LoginPageView(request):
    return render(request, "pages/login.html", {})
def BigJohn(request):
    return render(request, "pages/BigJohn.html", {})
def ArtSmart(request):
    return render(request, "pages/ArtSmart.html", {})
def CentralBank(request):
    return render(request, "pages/CentralBank.html", {})
def Engineer(request):
    return render(request, "pages/EngineersWorkshop.html", {})
def FamilyPlay(request):
    return render(request, "pages/FamilyPlay.html", {})
def Farm(request):
    return render(request, "pages/Farm.html", {})
def Firehouse(request):
    return render(request, "pages/Firehouse.html", {})
def Forts(request):
    return render(request, "pages/Forts.html", {})
def Hospital(request):
    return render(request, "pages/Hospital.html", {})
def IceCream(request):
    return render(request, "pages/IceCream.html", {})
def KidsPort(request):
    return render(request, "pages/Kidsport.html", {})
def LearningCenter(request):
    return render(request, "pages/LearningCenter.html", {})
def OceanSandbox(request):
    return render(request, "pages/OceanSandbox.html", {})
def PizzaPlace(request):
    return render(request, "pages/PizzaPlace.html", {})
def PartyPlace(request):
    return render(request, "pages/PartyPlace.html", {})
def Publix(request):
    return render(request, "pages/Publix.html", {})
def Theater(request):
    return render(request, "pages/Theater.html", {})
def TugBoats(request):
    return render(request, "pages/Tugboats.html", {})
def Vet(request):
    return render(request, "pages/Vet.html", {})
def Waters(request):
    return render(request, "pages/Waters.html", {})
def GuestServices(request):
    return render(request, "pages/GuestServices.html", {})
def Temp(request):
    return render(request, "pages/TempExhibit.html", {})
def FamilyPlayProject(request):
    return render(request, "pages/FamilyPlay.html", {})
def GlobalCafe(request):
    return render(request, "pages/GlobalCafe.html", {})
def SafetyVillage(request):
    return render(request, "pages/SafetyVillage.html", {})
def Play(request):
    return render(request, "pages/Play.html", {})
def Resources(request):
    return render(request, "pages/Resources.html", {})








