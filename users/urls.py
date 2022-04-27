from django.urls import include, re_path
from users.views import RegisterView

urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^register/", RegisterView.as_view(), name="register"),
]
