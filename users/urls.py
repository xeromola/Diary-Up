from django.urls import path
from users.views import RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password_change", auth_views.PasswordChangeView.as_view(),
         name="password_change"),
    path("password_change/done", auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
    path("register/", RegisterView.as_view(), name="register"),
]
