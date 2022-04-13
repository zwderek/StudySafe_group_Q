from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

class Members(APIView):

    def get(self, request):
        members = HKU_member.objects.all()
        data = HKU_memberSerializer(members, many=True)
        return Response(data.data)

    def post(self, request):
        member = HKU_memberSerializer(data=request.data)
        if member.is_valid():
            member.save()
            return Response(member.data, status=201)
        return Response(member.errors, status=400)

class Member(APIView):

    def get(self, request, pk):
        try:
            member = HKU_member.objects.get(hku_id=pk)
        except HKU_member.DoesNotExist:
            return HttpResponse(status=404)
        data = HKU_memberSerializer(member)
        return Response(data.data)

class HKU_Venues(APIView):

    def get(self, request):
        venues = Venue.objects.all()
        data = VenueSerializer(venues, many=True)
        return Response(data.data)

    def post(self, request):
        data = VenueSerializer(data=request.data)
        venue = VenueSerializer(data=data)
        if venue.is_valid():
            venue.save()
            return Response(venue.data, status=201)
        return Response(venue.errors, status=400)

class HKU_Venue(APIView):

    def get(self, request, pk):
        try:
            venue = Venue.objects.get(venue_code=pk)
        except Venue.DoesNotExist:
            return HttpResponse(status=404)
        data = VenueSerializer(venue)
        return Response(data.data)

class Entry_Exits(APIView):

    def get(self, request):
        ees = EntryExit.objects.all()
        data = EntryExitSerializer(ees, many=True)
        return Response(data.data)

    def post(self, request):
        data = EntryExitSerializer(data=request.data)
        ee = EntryExitSerializer(data=data)
        if ee.is_valid():
            ee.save()
            return Response(ee.data, status=201)
        return Response(ee.errors, status=400)
