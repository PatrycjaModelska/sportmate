from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.EventsList.as_view(), name='events_list'),
]

