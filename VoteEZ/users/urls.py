from django.urls import path
from .views import RegisterView, UserLogin, HomeView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home' ),
    path("login/", UserLogin.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout")
]