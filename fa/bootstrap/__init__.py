# -*- coding: utf-8 -*-
from pyramid_formalchemy import events
from fa.bootstrap import fanstatic_resources


#object listening rendering events
@events.subscriber([object, events.IBeforeListingRenderEvent])
def before_object_listing_render(context, event):
    fanstatic_resources.listing.need()

def includeme(config):
    config.include('fa.jquery')
    config.override_asset(
        to_override="fa.jquery:templates/admin/",
        override_with="fa.bootstrap:templates/admin/")
    config.override_asset(
        to_override="fa.jquery:templates/forms/",
        override_with="fa.bootstrap:templates/forms/")

