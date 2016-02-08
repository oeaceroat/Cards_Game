from django.conf.urls import url
from cardsGame import views

urlpatterns = [
    url(r'^cardsGame/users/$', views.user_list),
    url(r'^cardsGame/players/$', views.player_list),
    url(r'^cardsGame/cards/$', views.card_list),
    url(r'^cardsGame/users/(?P<userName>[a-z0-9]+)/$', views.user_detail),
    url(r'^cardsGame/players/(?P<userName>[a-z0-9]+)/$', views.player_detail),
    url(r'^cardsGame/cards/(?P<acc_name>[a-z0-9]+)/$', views.cards_count),
    url(r'^cardsGame/cards/(?P<userName>[a-z0-9]+)/$', views.card_detail),
]
