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
    path('api/entryexit/<str:hku_id>/<str:venue_id>/<str:time>/', api_views.Entry_Exit.as_view()),
    #<str:time> may need to be converted in the track by the documented code below

    path('api/venues-visited-by/<str:id>/<str:date>/', api_views.Visited_Venues.as_view()),
    path('api/close-contacts/<str:id>/<str:date>/', api_views.Close_Contacts.as_view()),
]
'''
from datetime import datetime
dt=datetime.now()
dt=dt+timedelta(hours=8)
time=dt.strftime("%Y-%m-%d %H:%M:%S")
'''
