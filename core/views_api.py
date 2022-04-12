from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *

class ContactView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = HKU_member.objects.all()
        return context

class VenueView(TemplateView):
    template_name = "venues.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['venues'] = Venue.objects.all()
        return context
