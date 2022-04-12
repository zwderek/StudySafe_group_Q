from django.urls import path
from core import api_views
from core import views_templates

urlpatterns = [
    path('api/venues', api_views.VenueList.as_view(), name='venue_list'),
    path('contacts', views_templates.ContactView.as_view()),
    path('venues', views_templates.VenueView.as_view()),
]