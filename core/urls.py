from django.urls import path
from core import views_templates

urlpatterns = [
    path('contacts', views_templates.ContactView.as_view()),
    path('venues', views_templates.VenueView.as_view()),
]
