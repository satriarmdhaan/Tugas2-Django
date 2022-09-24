from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import show_watchlist_json
from mywatchlist.views import show_watchlist_xml
from mywatchlist.views import show_watchlist_xml_by_id
from mywatchlist.views import show_watchlist_json_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('html/', show_watchlist, name='show_watchlist'),
    path('xml/', show_watchlist_xml, name='show_watchlist_xml'),
    path('json/', show_watchlist_json, name='show_watchlist_json'),
    path('json/<int:id>', show_watchlist_json_by_id, name='show_watchlist_json_by_id'),
    path('xml/<int:id>', show_watchlist_xml_by_id, name='show_watchlist_xml_by_id'),
]