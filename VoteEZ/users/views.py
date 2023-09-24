from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import resolve_url, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .forms import RegisterForm, UserAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages


# Create your views here.

class RegisterView(CreateView):
    template_name = "signup.html"
    form_class = RegisterForm
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        else:
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        auth_login(self.request, self.object)
        return response


class HomeView(TemplateView):
    template_name = "dashboard.html"


class UserLogin(LoginView):
    redirect_authenticated_user = True
    template_name = 'signin.html'
    form_class = UserAuthenticationForm


    def get_success_url(self):
        return reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        else:
            return super().get(request, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid email or password")
        return self.render_to_response(self.get_context_data(form=form))


class HomepageView(TemplateView):
    template_name = 'homepage.html'
