# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554838588.7441175
_enable_loop = True
_template_filename = 'C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/catalog/templates/prescriber.html'
_template_uri = 'prescriber.html'
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
        prescribers = context.get('prescribers', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
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
        prescribers = context.get('prescribers', UNDEFINED)
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n        <h1>Prescriber Detail Page</h1>\r\n        <table>\r\n            <tr style="font-size: 20px;">\r\n                <th>Prescriber First Name</th>\r\n                <th>Prescriber Last Name</th>\r\n                <th>Prescriber Type</th>\r\n            </tr>\r\n')
        for prescriber in prescribers:
            __M_writer('                <tr>\r\n                    <th>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.first_name ))
            __M_writer('</th>\r\n                    <th>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.last_name ))
            __M_writer('</th>\r\n')
            if prescriber.is_opioid_prescriber == 0:
                __M_writer('                        <th>Non-opioid Prescriber</th>\r\n')
            else:
                __M_writer('                        <th>Opioid Prescriber</th>\r\n')
            __M_writer('                </tr>     \r\n')
        __M_writer('        </table>\r\n        \r\n    </div>\r\n  \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/catalog/templates/prescriber.html", "uri": "prescriber.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "48": 3, "56": 3, "57": 12, "58": 13, "59": 14, "60": 14, "61": 15, "62": 15, "63": 16, "64": 17, "65": 18, "66": 19, "67": 21, "68": 23, "74": 68}}
__M_END_METADATA
"""
