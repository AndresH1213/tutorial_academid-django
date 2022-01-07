from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Meetup, Participant
from .forms import RegistrationsForm

# Create your views here.

def index(request):
    # meetups = [
    #     {'title': 'A first Meetup', 'location': 'New York', 'slug':'a-first-meetup'}, #the slug is like and id, unique identifier
    #     {'title': 'A second Meetup', 'location': 'Paris', 'slug': 'a-second-meetup'}  # item, but is more friendly readible for humans
    # ]
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        # 'show_meetups': 1,
        'meetups': meetups
    })

def meetup_details(request, meetup_slug):  
    # selected_meetup = {'title': 'A First Meetup', 'description': 'This is the first meetup!'}
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationsForm()
        else:
            registration_form = RegistrationsForm(request.POST)
            if registration_form.is_valid():
                # participant = registration_form.save()
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email) #returns (participant , created)
                selected_meetup.partipants.add(participant)
                return redirect(to='confirm-registration', meetup_slug=meetup_slug)

        
        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form
                })

    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        } )

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_model
    })
