# -*- coding: utf-8 -*-
from pyramid_formalchemy.views import ModelView as Base
from fa.bootstrap import actions

class ModelView(Base):

    defaults_actions = actions.defaults_actions

    pager_args = dict(link_attr={'class': ''},
                      curpage_attr={'class': 'active'},
                      format="~3~")

    def update_grid(self, grid):
        pass
