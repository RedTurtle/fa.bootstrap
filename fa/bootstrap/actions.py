from pyramid_formalchemy.i18n import _
from pyramid_formalchemy import actions
from pyramid_formalchemy.actions import Actions
from webhelpers.html import literal


class RealButton(actions.Action):
    body = '<button class="${_class}" tal:attributes="%(attributes)s">' \
           '<span tal:condition="action.icon" class="${action.icon}"></span> ${content}</button>'

    @property
    def icon(self):
        return self.rcontext.get('icon', None)


class UIButton(actions.UIButton):
    """Overwrite default pyramid_formalchemy action to support bootstrap style."""

    body = '<a class="${_class}" tal:attributes="%(attributes)s">' \
           '<span tal:condition="action.icon" class="${action.icon}"></span> ${content}</a>'

    @property
    def icon(self):
        return self.rcontext.get('icon', None)


class TabAction(actions.Action):
    """New action type - comaptible with boostrap style."""
    body = u"<li tal:attributes=\"class action.is_active(request) and 'active' or ''\">" \
           u'<a tal:attributes="%(attributes)s">${content}</a></li>'

    def is_active(self, request):
        for _id in self.rcontext.get('children', ()):
            if _id in request.matchdict.get('traverse'):
                return True
        return request.path_url.strip('/') == eval(self.attrs['href']).strip('/')


class BreadcrumbAction(TabAction):
    body = u'''<li tal:attributes="class action.is_active(request) and \'active\' or \'\'">
                    <a tal:condition="not action.is_active(request)" tal:attributes="%(attributes)s">${content}</a>
                    <span tal:condition="action.is_active(request)" tal:omit-tag="">${content}</span>
                    <span tal:condition="not action.is_active(request)" class="divider">/</span>
               </li>'''


class TabsActions(Actions, actions.Action):
    body = '''<ul class="nav nav-tabs">${items}</ul>'''

    def __init__(self, *args, **kwargs):
        Actions.__init__(self, *args, **kwargs)
        actions.Action.__init__(self, 'tabs', **kwargs)

    def render(self, request, **kwargs):
        items = Actions.render(self, request, **kwargs)
        self.rcontext.update(items=literal(items))
        return actions.Action.render(self, request)


class PillsActions(TabsActions):
    body = '''<ul class="nav nav-pills">${items}</ul>'''


class DropdownActions(Actions, actions.Action):
    """New action type - comaptible with boostrap style."""
    body = u'''<li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown">${content}<b class="caret"></b></a>
                    <ul class="dropdown-menu">
                        ${items}
                    </ul>
               </li>'''

    def __init__(self, *args, **kwargs):
        Actions.__init__(self, *args, **kwargs)
        actions.Action.__init__(self, **kwargs)

    def render(self, request, **kwargs):
        items = Actions.render(self, request, **kwargs)
        self.rcontext.update(items=literal(items))
        return actions.Action.render(self, request)


new = UIButton(
    id='new',
    content=_('New ${model_label}'),
    permission='new',
    _class='btn btn-primary',
    icon='glyphicon glyphicon-plus',
    attrs=dict(href="request.fa_url(request.model_name, 'new')"),
)

save = RealButton(
    id='save',
    type='submit',
    content=_('Save'),
    permission='edit',
    _class='btn btn-success',
    icon='glyphicon glyphicon-ok',
)

save_and_add_another = UIButton(
    id='save_and_add_another',
    content=_('Save and add another'),
    permission='edit',
    _class='btn btn-success',
    icon='glyphicon glyphicon-plus',
    attrs=dict(onclick=("var f = jQuery(this).parents('form');"
                        "jQuery('#next', f).val(window.location.href);"
                        "f.submit();")),
)

edit = UIButton(
    id='edit',
    content=_('Edit'),
    permission='edit',
    _class='btn btn-info',
    icon='glyphicon glyphicon-edit',
    attrs=dict(href="request.fa_url(request.model_name, request.model_id, 'edit')"),
)

back = UIButton(
    id='back',
    content=_('Back'),
    _class='btn btn-default',
    attrs=dict(href="request.fa_url(request.model_name)"),
)

delete = UIButton(
    id='delete',
    content=_('Delete'),
    permission='delete',
    _class='btn btn-danger',
    icon='glyphicon glyphicon-trash',
    attrs=dict(onclick=("var f = jQuery(this).parents('form');"
                        "f.attr('action', window.location.href.replace('/edit', '/delete'));"
                        "f.submit();")),
)

cancel = UIButton(
    id='cancel',
    content=_('Cancel'),
    permission='view',
    _class='btn btn-default',
    icon='glyphicon glyphicon-remove',
    attrs=dict(href="request.fa_url(request.model_name)"),
)

defaults_actions = actions.defaults_actions.copy()
defaults_actions['listing_buttons'] = Actions(new)
defaults_actions['new_buttons'] = Actions(save, save_and_add_another, cancel)
defaults_actions['edit_buttons'] = Actions(save, delete, cancel)
defaults_actions['show_buttons'] = Actions(edit, back)
