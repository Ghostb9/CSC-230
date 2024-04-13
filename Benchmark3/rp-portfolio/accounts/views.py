#########################
#####
##### VIEWS FOR ALL ACCOUNTS MADE
#####
#########################



from django.contrib.auth import login
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'pages/login.html'  # Path to your login template
    redirect_authenticated_user = True  # Redirect users who are already logged in
    next_page = reverse_lazy('home')  # Redirect to homepage upon successful login

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user
            send_mail(
                'Welcome to our site!',
                f'Hi {user.username}, thank you for registering with our site.',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            print("Redirecting to home.")  # Debug print
            return redirect('home')
        else:
            print("Form is not valid:", form.errors)  # Print form errors for debugging
    else:
        form = UserRegisterForm()
    return render(request, 'pages/signup.html', {'form': form})


# views.py in your app


def custom_logout(request):
    next_page = request.GET.get('next', reverse_lazy('home'))
    return LogoutView.as_view(next_page=next_page)(request)
