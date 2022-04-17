from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from datetime import datetime

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

class Entry_Exit(APIView):#API8

    def post(self, request, hku_id, venue_id, time):
        try:
            ees = EntryExit.objects.filter(member=hku_id, venue=venue_id)
        except EntryExit.DoesNotExist:
            ee=EntryExit.objects.create(member=hku_id, venue=venue_id, enter_time=time, exit_time="1111-11-11 11:11:11")
            ees = EntryExit.objects.all()
            data = EntryExitSerializer(ees, many=True)
            return Response(data.data, status=201)
        found=False
        for ee in ees:
            if ee.exit_time=="1111-11-11 11:11:11":
                ee.exit_time=time
                ee.save()
                found=True
                break
        if not found:
            ee=EntryExit.objects.create(member=hku_id, venue=venue_id, enter_time=time, exit_time="1111-11-11 11:11:11")
        ees = EntryExit.objects.all()
        data = EntryExitSerializer(ees, many=True)
        if found:
            return Response(data.data, status=200)
        else:
            return Response(data.data, status=201)

class Visited_Venue(APIView):

    def get(self, request, id, date):
        end_date = datetime.strptime(date, "%Y-%m-%d")
        start_date = end_date + timedelta(days=-2)
        queryset = EntryExit.objects.filter(member_id=id).\
                    filter(enter_time__range=(start_date, end_date + timedelta(days=1))).\
                    order_by('enter_time')
        serializer = EntryExitSerializer(queryset, many=True)
        return Response(["Venue code: "+i['venue']+" Enter time: "+i['enter_time']+" Exit time: "+i['exit_time'] for i in serializer.data])
