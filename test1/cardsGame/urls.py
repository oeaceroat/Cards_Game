from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from rest_framework.urlpatterns import format_suffix_patterns

from cardsGame.views import card_view, player_view, user_view, bundle_view

urlpatterns = [
    url(r'^cardsGame/users/$', user_view.user_list),
    url(r'^cardsGame/players/$', player_view.player_list),
    url(r'^cardsGame/cards/$', card_view.card_list),
    url(r'^cardsGame/bundles/$', bundle_view.bundle_list),
    url(r'^cardsGame/users/(?P<userName>[a-z0-9]+)/$', user_view.user_detail),
    url(r'^cardsGame/players/(?P<userName>[a-z0-9]+)/$', player_view.player_detail),
    url(r'^cardsGame/cards/(?P<acc_name>[a-z0-9]+)/$', card_view.cards_count),
    url(r'^cardsGame/cards/(?P<userName>[a-z0-9]+)/$', card_view.card_detail),
    url(r'^cardsGame/bundles/(?P<acc_name>[a-z0-9]+)/$', bundle_view.bundle_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])