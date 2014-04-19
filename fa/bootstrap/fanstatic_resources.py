from fanstatic import Group, Library, Resource
from js.jquery import jquery
from js.jqueryui import jqueryui
from js.bootstrap import bootstrap as bootstrap_orig
from js.jquery_tablesorter import tablesorter
from fa.jquery.fanstatic_resources import fa_js

fa_bootstrap_library = Library('fa_bootstrap', 'static')
listing = Resource(fa_bootstrap_library, 'js/listing.js', depends=[jquery])
autocomplete = Resource(fa_bootstrap_library, 'js/autocomplete.js', depends=[jqueryui, fa_js])


# bootstrap-select
select_picker_js = Resource(fa_bootstrap_library, 'js/bootstrap-select.js', depends=[bootstrap_orig],
                      minified='js/bootstrap-select.min.js')
select_picker_css = Resource(fa_bootstrap_library, 'css/bootstrap-select.css')
bselect_initializer = Resource(fa_bootstrap_library, 'bootstrap_select/..',
                               renderer=lambda _: "<script>$(function(){$('.selectpicker').selectpicker()})</script>")
select_picker = Group([select_picker_js, select_picker_css, bselect_initializer])


# dual list box
duallistbox_js = Resource(fa_bootstrap_library, 'js/jquery.bootstrap-duallistbox.js', depends=[bootstrap_orig],
                          minified='js/jquery.bootstrap-duallistbox.min.js')
duallistbox_css = Resource(fa_bootstrap_library, 'css/bootstrap-duallistbox.css')
duallistbox_initializer_renderer = lambda _: "<script>$(function(){$('.duallistbox').bootstrapDualListbox()})</script>"
duallistbox_initializer = Resource(fa_bootstrap_library, 'dual_init/..', renderer=duallistbox_initializer_renderer)
duallistbox = Group([duallistbox_js, duallistbox_css, duallistbox_initializer])


bootstrap = Group([listing, bootstrap_orig, tablesorter])
