from django.urls import path
from .views import *

urlpatterns = [
    path("sign_in/", sign_in, name="signin"),
    path("sign_up/", sign_up, name="signup"),
    path("sign_out/", SignOut),
]
