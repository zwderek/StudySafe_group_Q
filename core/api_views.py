from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.views.generic import View
from .models import *
from .serializers import *
from rest_framework import serializers
from rest_framework.parsers import JSONParser
# Create your views here.
class Members(View):
    def get(self, request):
        members=HKU_member.objects.all()
        data=serializers.HKU_memberSerializer(members,many=True)
        return JsonResponse(data.data, safe=False)
    def post(self, request):
        data = JSONParser().parse(request)
        member = serializers.HKU_memberSerializer(data=data)
        if member.is_valid():
            member.save()
            return JsonResponse(member.data, status=201)
        return JsonResponse(member.errors, status=400)
class Member(View):
    def get(self, request, pk):
        try:
            member=HKU_member.objects.get(hku_id=pk)
        except HKU_member.DoesNotExist:
            return HttpResponse(status=404)
        data = serializers.HKU_memberSerializer(member)
        return JsonResponse(data.data)
class HKU_Venues(View):
    def get(self, request):
        venues=Venue.objects.all()
        data=serializers.VenueSerializer(venues,many=True)
        return JsonResponse(data.data, safe=False)
    def post(self, request):
        data = JSONParser().parse(request)
        venue = serializers.VenueSerializer(data=data)
        if venue.is_valid():
            venue.save()
            return JsonResponse(venue.data, status=201)
        return JsonResponse(venue.errors, status=400)
class HKU_Venue(View):
    def get(self, request, pk):
        try:
            venue=Venue.objects.get(venue_code=pk)
        except Venue.DoesNotExist:
            return HttpResponse(status=404)
        data = serializers.VenueSerializer(venue)
        return JsonResponse(data.data)
class Entry_Exits(View):
    def get(self, request):
        ees=EntryExit.objects.all()
        data=serializers.EntryExitSerializer(ees,many=True)
        return JsonResponse(data.data, safe=False)
    def post(self, request):
        data = JSONParser().parse(request)
        ee = serializers.EntryExitSerializer(data=data)
        if ee.is_valid():
            ee.save()
            return JsonResponse(ee.data, status=201)
        return JsonResponse(ee.errors, status=400)
