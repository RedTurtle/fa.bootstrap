from paste.util.template import paste_script_template_renderer
from pyramid.scaffolds import PyramidTemplate

class PyramidFormAlchemyBootstrapTemplate(PyramidTemplate):
    _template_dir = ('pyramid_fa_bootstrap')
    summary = "Pyramid SQLAlchemy project using fa.bootstrap"
    template_renderer = staticmethod(paste_script_template_renderer)
