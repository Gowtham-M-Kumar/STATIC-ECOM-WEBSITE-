from django.urls import path
from . import views
from .views import home_view
urlpatterns = [
    path('HOME/', home_view),  # Home page
]