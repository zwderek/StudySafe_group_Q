from django.urls import path
from core import views_api

urlpatterns = [
    path('contacts', views_api.ContactView.as_view()),
    path('venues', views_api.VenueView.as_view()),
]