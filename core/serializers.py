from rest_framework import serializers
from .models import *


class HKU_memberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = '__all__'

class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = HKU_member
        fields = '__all__'

class EntryExitSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntryExit
        fields = '__all__'