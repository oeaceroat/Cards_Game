from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cardsGame.views import card_view, player_view, user_view, bundle_view

urlpatterns = [
    url(r'^cardsGame/users/$', user_view.UserList.as_view()),
    url(r'^cardsGame/players/$', player_view.PlayerList.as_view()),
    url(r'^cardsGame/cards/$', card_view.CardList.as_view()),
    url(r'^cardsGame/bundles/$', bundle_view.BundleList.as_view()),
    url(r'^cardsGame/users/(?P<userName>[a-z0-9]+)/$', user_view.UserDetail.as_view()),
    url(r'^cardsGame/players/(?P<userName>[a-z0-9]+)/$', player_view.PlayerDetail.as_view()),
    url(r'^cardsGame/cards/(?P<acc_name>[a-z0-9]+)/$', card_view.cards_count),
    url(r'^cardsGame/cards/(?P<userName>[a-z0-9]+)/$', card_view.CardDetail.as_view()),
    url(r'^cardsGame/bundles/(?P<acc_name>[a-z0-9]+)/$', bundle_view.BundleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)