from django.urls import path
from . import views

'''
    slug tells django that de dynamic value we have after two colons, should match the format lowercase no spaces
    just dashes and so on and it will be treated as such by django internally, we don't have to add this but we can add it for
    even better support of the slug feature as a identifier in the url.
'''

urlpatterns = [
    path('', views.index, name='all-meetups' ), # our-domain.com/meetups
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'), # before of dynamic path cuz sucess might be confused with the slug
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail') #our-domain.com/meetups/<dynamic-path-segment>
]