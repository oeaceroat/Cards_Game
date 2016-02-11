from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cardsGame.views import card_view, player_view, user_view, bundle_view

urlpatterns = [
    url(r'^cardsGame/users/$', user_view.UserList.as_view()), #List all users or create new user
    url(r'^cardsGame/players/$', player_view.PlayerList.as_view()), #List all players or create new player
    url(r'^cardsGame/cards/$', card_view.CardList.as_view()), #List all cards or create new card
    url(r'^cardsGame/bundles/$', bundle_view.BundleList.as_view()), #List all bundles or create new bundle
    url(r'^cardsGame/users/(?P<userName>[a-z0-9]+)/$', user_view.UserDetail.as_view()), #Show details of user by userName
    url(r'^cardsGame/players/(?P<userName>[a-z0-9]+)/$', player_view.PlayerDetail.as_view()), # #Show details of players by userName
    url(r'^cardsGame/cards/(?P<acc_name>[a-z0-9]+)/$', card_view.cards_count), #Show count of cards by acc_name
    url(r'^cardsGame/cards/(?P<acc_name>[a-z0-9]+)/$', card_view.CardDetail.as_view()), #Show details of cards by acc_name
    url(r'^cardsGame/bundles/(?P<acc_name>[a-z0-9]+)/$', bundle_view.BundleDetail.as_view()), #Show details of bundles by acc_name
    url(r'^cardsGame/bundles/(?P<bundle_source_id>[a-z0-9]+)/(?P<bundle_destination_id>[a-z0-9]+)/$', bundle_view.bundle_merge), #Put elemente of source bundle into destinations bundle
]

urlpatterns = format_suffix_patterns(urlpatterns)