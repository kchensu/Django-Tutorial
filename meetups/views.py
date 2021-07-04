from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    meetups = [
        {'title': 'A First Meetup', 'location': "Vancouver", 'slug': 'a-first-meetup'},
        {'title': 'A Second Meetup', 'location': "Calgary", 'slug': 'a-second-meetup'},
        {'title': 'A Thrid Meetup', 'location': 'Toronto', 'slug': 'a-third-meetup'},
        {'title': 'A Fourth Meetup', 'location': 'Montreal', 'slug': 'a-fourth-meetup'},
        {'title': 'A Fifth Meetup', 'location': 'St. Johns', 'slug': 'a-fifth-meetup'},
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    selected_meetup = {'title': 'A First Meetup',
                       'description': 'This is the first meetup!'}
    return render(request, 'meetups/meetup_details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })
