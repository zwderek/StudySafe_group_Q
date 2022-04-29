from django.contrib import admin
from .models import *

class HKU_MemberAdmin(admin.ModelAdmin):
    list_display = ('hku_id', 'name')

class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_code', 'location', 'type', 'capacity')

class EntryExitAdmin(admin.ModelAdmin):
    list_display = ('member', 'venue', 'enter_time', 'exit_time')

admin.site.register(HKU_member, HKU_MemberAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(EntryExit, EntryExitAdmin)

