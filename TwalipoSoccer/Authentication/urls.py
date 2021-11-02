from Authentication.views import LandingPage
from django.urls import path

urlpatterns = [
    path(r'', LandingPage.as_view()),
]