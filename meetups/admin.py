from django.contrib import admin
from .models import Meetup, Location, Participant
# Register your models here.

class meetupAdmid(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup, meetupAdmid)
admin.site.register(Location)
admin.site.register(Participant)