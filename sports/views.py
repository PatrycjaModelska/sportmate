from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import ListView

from sports.models import Event, Sport


# manage posts

class EventsList(ListView):
    model = Event
    template_name = "events_list.html"
    context_object_name = "events"
    ordering = ['-when']

