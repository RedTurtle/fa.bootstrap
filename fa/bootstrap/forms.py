from formalchemy import FieldSet, fatypes
from fa.bootstrap import renderers


class BootstrapFieldSet(FieldSet):
    default_renderers = dict(FieldSet.default_renderers)
    default_renderers.update({
        fatypes.String: renderers.BootstrapTextFieldRenderer,
        fatypes.Unicode: renderers.BootstrapTextFieldRenderer,
        fatypes.Text: renderers.BootstrapTextFieldRenderer,
        fatypes.Integer: renderers.BootstrapIntegerFieldRenderer,
        fatypes.Float: renderers.BootstrapFloatFieldRenderer,
        fatypes.Numeric: renderers.BootstrapFloatFieldRenderer,
        fatypes.Interval: renderers.BootstrapIntervalFieldRenderer,
        fatypes.Boolean: renderers.BootstrapBooleanFieldRenderer,
        fatypes.Set: renderers.BootstrapSelectFieldRenderer,
        fatypes.List: renderers.BootstrapSelectFieldRenderer,
        'dropdown': renderers.BootstrapSelectFieldRenderer,
    })
