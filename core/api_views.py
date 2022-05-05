from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from datetime import datetime, timedelta
import pytz

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
        venue = VenueSerializer(data=request.data)
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
            ees = EntryExit.objects.filter(member=HKU_member.objects.get(hku_id=hku_id), venue=Venue.objects.get(venue_code=venue_id))
        except EntryExit.DoesNotExist:
            ee=EntryExit.objects.create(member=HKU_member.objects.get(hku_id=hku_id), venue=Venue.objects.get(venue_code=venue_id), enter_time=time, exit_time="1111-11-11 11:11:11")
            ees = EntryExit.objects.all()
            data = EntryExitSerializer(ees, many=True)
            return Response(data.data, status=201)
        found=False
        try:
            ee=EntryExit.objects.get(exit_time="1111-11-11T11:11:11Z")
        except EntryExit.DoesNotExist:
            ee=EntryExit.objects.create(member=HKU_member.objects.get(hku_id=hku_id), venue=Venue.objects.get(venue_code=venue_id), enter_time=time, exit_time="1111-11-11 11:11:11")
            ees = EntryExit.objects.all()
            data = EntryExitSerializer(ees, many=True)
            return Response(data.data, status=201)
        ee.exit_time=time
        ee.save()
        ees = EntryExit.objects.all()
        data = EntryExitSerializer(ees, many=True)
        return Response(data.data, status=200)

def get_visited_venues(id, date):
    end_date = datetime.strptime(date, "%Y-%m-%d")
    start_date = end_date + timedelta(days=-2)
    queryset = EntryExit.objects.filter(member_id=id). \
        filter(enter_time__range=(start_date, end_date + timedelta(days=1))). \
        order_by('enter_time')
    serializer = EntryExitSerializer(queryset, many=True)
    return serializer.data

def check_contact_time(enter_time, exit_time, po_enter_time, po_exit_time):
    utc = pytz.UTC
    enter_time = enter_time.replace(tzinfo=utc)
    exit_time = exit_time.replace(tzinfo=utc)
    #enter = datetime.strptime(enter_time, "%Y-%m-%d %H:%M:%S")
    #exit = datetime.strptime(exit_time, "%Y-%m-%d %H:%M:%S")
    po_enter = datetime.strptime(po_enter_time, "%Y-%m-%dT%H:%M:%SZ")
    po_exit = datetime.strptime(po_exit_time, "%Y-%m-%dT%H:%M:%SZ")

    po_enter = po_enter.replace(tzinfo=utc)
    po_exit = po_exit.replace(tzinfo=utc)

    if min(exit_time, po_exit) - max(enter_time, po_enter) >= timedelta(minutes=30):
        return True
    else:
        return False

def get_close_contacts(id, date):
    close_contact_list = set()
    visited_venue_list = get_visited_venues(id, date)
    for event in visited_venue_list:
        this_member = event['member']
        this_venue = event['venue']
        this_in = event['enter_time']
        this_out = event['exit_time']
        queryset = EntryExit.objects.exclude(member=this_member).filter(venue=this_venue)
        res = EntryExitSerializer(queryset, many=True)
        for i in queryset:
            if (check_contact_time(i.enter_time, i.exit_time, this_in, this_out)):
            #if (check_contact_time(i['enter_time'], i['exit_time'], this_in, this_out)):
                close_contact_list.add(i.member)

    #print("!!!!!!!!!")
    #print(close_contact_list)

    _queryset = HKU_member.objects.filter(hku_id=-1)
    for i in close_contact_list:
        _queryset |= HKU_member.objects.filter(hku_id=i.hku_id)
    serializer = HKU_memberSerializer(_queryset, many=True)
    return serializer.data


class Visited_Venues(APIView):

    def get(self, request, id, date):
        data = get_visited_venues(id, date)
        return Response(data)
        '''
        return Response(["Venue code: " + i['venue'] +
                         " Enter time: " + i['enter_time'] +
                         " Exit time: " + i['exit_time'] for i in data])
        '''

class Close_Contacts(APIView):

    def get(self, rquest, id, date):

        return Response(get_close_contacts(id, date))
