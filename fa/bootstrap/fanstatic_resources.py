from fanstatic import Group, Library, Resource
from js.jquery import jquery
from js.bootstrap import bootstrap as js_bootstrap
from js.jquery_tablesorter import tablesorter

fa_bootstrap_library = Library('fa_bootstrap', 'static')
listing = Resource(fa_bootstrap_library, 'js/listing.js', depends=[jquery])

bootstrap = Group([listing, js_bootstrap, tablesorter])
