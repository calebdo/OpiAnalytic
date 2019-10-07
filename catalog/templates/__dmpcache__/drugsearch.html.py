# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554846104.1131637
_enable_loop = True
_template_filename = 'C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/catalog/templates/drugsearch.html'
_template_uri = 'drugsearch.html'
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
        drugs = context.get('drugs', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        numresults = context.get('numresults', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        drugs = context.get('drugs', UNDEFINED)
        def site_center():
            return render_site_center(context)
        numresults = context.get('numresults', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n        <h1>Drug Search Results</h1>\r\n        <h4>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( numresults ))
        __M_writer(' results found</h4><br>\r\n        <table>\r\n            <tr class="heading-title">\r\n                <th>Drug Name</th>\r\n                <th>Drug Type</th>\r\n            </tr>\r\n')
        for drug in drugs:
            __M_writer('                <tr>\r\n                    <th>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drug.name ))
            __M_writer('</th>\r\n')
            if drug.is_opioid == 0:
                __M_writer('                        <th>Non-opioid</th>\r\n')
            else:
                __M_writer('                        <th>Opioid</th>\r\n')
            __M_writer('                </tr>     \r\n')
        __M_writer('        </table>\r\n        \r\n    </div>\r\n  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/catalog/templates/drugsearch.html", "uri": "drugsearch.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "49": 3, "58": 3, "59": 6, "60": 6, "61": 12, "62": 13, "63": 14, "64": 14, "65": 15, "66": 16, "67": 17, "68": 18, "69": 20, "70": 22, "76": 70}}
__M_END_METADATA
"""
