# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554746809.297236
_enable_loop = True
_template_filename = 'C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'navbar_items', 'login_navbar', 'header_maintenance', 'site_left']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        def login_navbar():
            return render_login_navbar(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        def header_maintenance():
            return render_header_maintenance(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'login_navbar'):
            context['self'].login_navbar(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_maintenance'):
            context['self'].header_maintenance(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('OpiAnalytics')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_items():
            return render_navbar_items(context)
        self = context.get('self', UNDEFINED)
        user = context.get('user', UNDEFINED)
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


def render_header_maintenance(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_maintenance():
            return render_header_maintenance(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer("\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "46": 1, "51": 3, "56": 17, "61": 21, "66": 25, "71": 29, "77": 3, "83": 3, "89": 5, "97": 5, "98": 9, "99": 9, "105": 19, "111": 19, "117": 23, "123": 23, "129": 27, "135": 27, "141": 135}}
__M_END_METADATA
"""
