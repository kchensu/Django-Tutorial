from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='name'),
    path('meetups/<slug:meetup_slug>',
         views.meetup_details, name='meetup_details')
]
