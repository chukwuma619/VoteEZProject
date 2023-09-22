from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import RegisterForm, UserAuthenticationForm
from django.contrib import messages


# Create your views here.

class RegisterView(FormView):
    template_name = "signup.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")


class UserLogin(LoginView):
    redirect_authenticated_user = True
    template_name = 'signin.html'
    form_class = UserAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('secret')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid email or password")
        return self.render_to_response(self.get_context_data(form=form))


class MySecretView(LoginRequiredMixin, TemplateView):
    template_name = "secret.html"


class HomepageView(TemplateView):
    template_name = 'homepage.html'
