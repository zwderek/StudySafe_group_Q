from django.template.defaulttags import url
from django.urls import path
from core import views_templates, api_views

urlpatterns = [

    path('contacts', views_templates.ContactView.as_view()),
    path('venues', views_templates.VenueView.as_view()),

    path('api/members/', api_views.Members.as_view()),
    path('api/members/<str:pk>/', api_views.Member.as_view()),
    path('api/venues/', api_views.HKU_Venues.as_view()),
    path('api/venues/<str:pk>/', api_views.HKU_Venue.as_view()),
    path('api/entryexit/', api_views.Entry_Exits.as_view()),
]