from django.conf.urls import url
from cardsGame.views import card_view, player_view, user_view

urlpatterns = [
    url(r'^cardsGame/users/$', user_view.user_list),
    url(r'^cardsGame/players/$', player_view.player_list),
    url(r'^cardsGame/cards/$', card_view.card_list),
    url(r'^cardsGame/users/(?P<userName>[a-z0-9]+)/$', user_view.user_detail),
    url(r'^cardsGame/players/(?P<userName>[a-z0-9]+)/$', player_view.player_detail),
    url(r'^cardsGame/cards/(?P<acc_name>[a-z0-9]+)/$', card_view.cards_count),
    url(r'^cardsGame/cards/(?P<userName>[a-z0-9]+)/$', card_view.card_detail),
]
