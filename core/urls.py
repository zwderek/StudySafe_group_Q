from django.urls import path
from core import views_templates

urlpatterns = [
    path('contacts', views_templates.ContactView.as_view()),
    path('venues', views_templates.VenueView.as_view()),
    url(r'^members/$', api_views.Members.as_view()),
    url(r'^members/(?P<pk>\d+)/$',api_views.Member.as_view()),
    url(r'^venues/$', api_views.HKU_Venues.as_view()),
    url(r'^venues/(?P<pk>\d+)/$',api_views.HKU_Venue.as_view()),
    url(r'^entryexit/$', api_views.Entry_Exits.as_view()),
]
