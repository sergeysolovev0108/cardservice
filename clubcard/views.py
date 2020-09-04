
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class GetClubCard(ListView):
    model = ClubCard
    template_name = 'base.html'
    context_object_name = 'clubcard'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def get_club_card(request, clubcard_id):
    clubcard = ClubCard.objects.get(pk=clubcard_id)
    return render(request, 'clubcard/single.html', {"clubcard": clubcard})



