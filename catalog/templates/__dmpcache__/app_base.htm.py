# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554849068.4979365
_enable_loop = True
_template_filename = 'C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_left', 'page_title', 'navbar_items', 'login_navbar']


from catalog import models as cmod 

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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def login_navbar():
            return render_login_navbar(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'login_navbar'):
            context['self'].login_navbar(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="category-list">\r\n    <h4>Search</h4>\r\n    <li><a style="padding-right: 5px;" class="dropdown-item" href="/catalog/search/">Drugs and Prescribers</a></li>\r\n    <h4>Analytics</h4>\r\n    <li><a style="padding-right: 5px;" class="dropdown-item" href="/catalog/analytics/">View Analytics</a></li>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('Opianalytics')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def navbar_items():
            return render_navbar_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n      \r\n        <li class="dropdown">\r\n          <a class="dropdown-toggle" data-toggle="dropdown" href="#">Welcome, ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( user.first_name ))
        __M_writer('\r\n          <span class="caret"></span></a>\r\n          <ul class="dropdown-menu">\r\n            <li><a class="dropdown-item" href="/account/index/">Account</a></li>\r\n            <li><a class="dropdown-item" href="/account/logout/">Logout</a></li>\r\n          </ul>\r\n        </li>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def login_navbar():
            return render_login_navbar(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <li><a class="dropdown-item" href="/account/login/">Login</a></li>\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/catalog/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "46": 1, "47": 2, "52": 12, "57": 14, "62": 28, "67": 33, "73": 5, "79": 5, "85": 14, "91": 14, "97": 16, "105": 16, "106": 20, "107": 20, "113": 31, "119": 31, "125": 119}}
__M_END_METADATA
"""
