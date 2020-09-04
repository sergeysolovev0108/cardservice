from django.urls import path

from .views import *

urlpatterns = [
    #path('', index, name='index'),
    path('', GetClubCard.as_view(), name='home'),
    path('clubcard/<int:clubcard_id>/', get_club_card, name='clubcard'),


]
