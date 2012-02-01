from fanstatic import Group, Library, Resource
from js.jquery import jquery
from js.jqueryui import jqueryui
from js.bootstrap import bootstrap_js
from js.jquery_tablesorter import tablesorter
from fa.jquery.fanstatic_resources import fa_js

fa_bootstrap_library = Library('fa_bootstrap', 'static')
listing = Resource(fa_bootstrap_library, 'js/listing.js', depends=[jquery])
alerts = Resource(fa_bootstrap_library, 'js/alerts.js', depends=[jquery])
autocomplete = Resource(fa_bootstrap_library, 'js/autocomplete.js', depends=[jqueryui, fa_js])

bootstrap = Group([listing, alerts, bootstrap_js, tablesorter])
