from django.urls import path
from core.views import HomeView

urlpatterns = [
    path("api/", HomeView.as_view())
]
