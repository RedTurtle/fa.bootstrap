from fanstatic import Group, Library, Resource
from js.jquery import jquery
from js.jqueryui import jqueryui
from js.bootstrap import bootstrap
from js.jquery_tablesorter import tablesorter
from fa.jquery.fanstatic_resources import fa_js

fa_bootstrap_library = Library('fa_bootstrap', 'static')
listing = Resource(fa_bootstrap_library, 'js/listing.js', depends=[jquery])
autocomplete = Resource(fa_bootstrap_library, 'js/autocomplete.js', depends=[jqueryui, fa_js])

bootstrap = Group([listing, bootstrap, tablesorter])
