# -*- coding: utf-8 -*-
from formalchemy import fields
from formalchemy import helpers as h
from fa.jquery import renderers
import fanstatic_resources
from formalchemy.exceptions import FieldNotFoundError


def AutocompleteRelationRenderer(filter_by='id', renderer=fields.IntegerFieldRenderer, **jq_options):
    """Use http://docs.jquery.com/UI/Autocomplete with pyramid"""

    class Renderer(renderer):

        def __init__(self, *args, **kwargs):
            super(Renderer, self).__init__(*args, **kwargs)
            self.field.render_opts['options'] = []

        def update_options(self, options, kwargs):
            kwargs['source'] = self.request.fa_url(
                self.field.relation_type().__name__, 'autocomplete')

        def render(self, **kwargs):
            fanstatic_resources.autocomplete.need()
            filter_value = self.jq_options.get('filter_by')
            if self.raw_value:
                label = getattr(self.raw_value, filter_value, u'Not selected')
            else:
                label = u''

            radio = h.radio_button(self.name, value=self.value, **kwargs)
            radio += h.literal('&nbsp;')
            radio += h.content_tag('span', label)
            children = h.content_tag("span", radio, class_="add-on")
            html = h.content_tag("div", children, class_="input-prepend")
            return ''.join(html)

        def _serialized_value(self):
            try:
                return super(Renderer, self)._serialized_value()
            except FieldNotFoundError:
                return None

    jq_options.update(filter_by=filter_by, show_input=True)

    return renderers.jQueryFieldRenderer('bootstrap_autocomplete_relation', renderer=Renderer, **jq_options)


@renderers.alias(AutocompleteRelationRenderer)
def autocomplete_relation():
    pass


class BootstrapFieldMixin(object):
    """
        Mixin to add `class="form-control"` to renderers
    """

    def render(self, **kwargs):
        if 'class' in kwargs:
            kwargs['class'] += ' form-control'
        else:
            kwargs['class'] = 'form-control'
        return super(BootstrapFieldMixin, self).render(**kwargs)


class BootstrapBooleanFieldRenderer(fields.CheckBoxFieldRenderer):
    def render(self, **kwargs):
        checkbox = super(BootstrapBooleanFieldRenderer, self).render(**kwargs)
        return '<span class="input-group" style="width:1px"><span class="input-group-addon">%s</span>' \
               '<span class="form-control">%s</span></span>' % (checkbox, 'True')


class BootstrapTextFieldRenderer(BootstrapFieldMixin, fields.TextFieldRenderer):
    pass


class BootstrapIntegerFieldRenderer(BootstrapFieldMixin, fields.IntegerFieldRenderer):
    pass


class BootstrapFloatFieldRenderer(BootstrapFieldMixin, fields.FloatFieldRenderer):
    pass


class BootstrapIntervalFieldRenderer(BootstrapFieldMixin, fields.IntervalFieldRenderer):
    pass


class BootstrapSelectFieldRenderer(BootstrapFieldMixin, fields.SelectFieldRenderer):
    def render(self, **kwargs):
        auto_width = kwargs.pop('width', None)
        if auto_width:
            kwargs['style'] = kwargs.get('style', '') + '; width: ' + str(auto_width)
        return super(BootstrapSelectFieldRenderer, self).render(**kwargs)
