# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554855453.8408706
_enable_loop = True
_template_filename = 'C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/catalog/templates/drug.html'
_template_uri = 'drug.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        details = context.get('details', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        relatedDrugs = context.get('relatedDrugs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        details = context.get('details', UNDEFINED)
        def site_center():
            return render_site_center(context)
        relatedDrugs = context.get('relatedDrugs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n        <h1>Drug Details</h1>\r\n        <table class="results">\r\n            <tr class="heading-title">\r\n                <th>Drug Name</th>\r\n                <th>Drug Type</th>\r\n                <th>Total Quantity Prescribed</th>\r\n            </tr>\r\n      \r\n            <tr>\r\n                <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( details.name ))
        __M_writer('</td>\r\n')
        if details.is_opioid == 0:
            __M_writer('                    <td>Non-opioid</td>\r\n')
        else:
            __M_writer('                    <td>Opioid</td>\r\n')
        __M_writer('                <td>###</td>\r\n            </tr>   \r\n        </table>       \r\n    </div>\r\n    <div class="col-md-6">\r\n        <h3>Related Drugs</h3>\r\n        <p>Prescribers who often prescribe ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( details.name ))
        __M_writer(' also prescribe these drugs:</p>\r\n        <ol>\r\n')
        for rd in relatedDrugs:
            __M_writer('                <li><a href="/catalog/drug/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( rd.id ))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( rd.name ))
            __M_writer('</a></li>\r\n')
        __M_writer('        </ol>\r\n    </div>\r\n      <div class="col-md-6">\r\n        <h3>Top Prescribers</h3>\r\n        <ol>\r\n           \r\n        </ol>\r\n    </div>\r\n  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/catalog/templates/drug.html", "uri": "drug.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "49": 3, "58": 3, "59": 14, "60": 14, "61": 15, "62": 16, "63": 17, "64": 18, "65": 20, "66": 26, "67": 26, "68": 28, "69": 29, "70": 29, "71": 29, "72": 29, "73": 29, "74": 31, "80": 74}}
__M_END_METADATA
"""
