# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554838201.6318133
_enable_loop = True
_template_filename = 'C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'header_maintenance', 'navbar_items', 'login_navbar', 'site_left', 'site_center']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def login_navbar():
            return render_login_navbar(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def header_maintenance():
            return render_header_maintenance(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n            <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('</title>\r\n        \r\n\r\n')
        __M_writer('        <script href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage\\media\\jquery-3.3.1.min.js"></script>\r\n        <script href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage\\media\\bootstrap-3.3.7-dist\\js\\bootstrap.min.js"></script>\r\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage\\media\\bootstrap-3.3.7-dist\\css\\bootstrap.min.css">\r\n        <link rel="icon" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/mountain.png">\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_maintenance'):
            context['self'].header_maintenance(**pageargs)
        

        __M_writer('\r\n       \r\n\r\n        <header>\r\n                <nav class="navbar">\r\n                        <div class="container-fluid" id="site_navbar_top">\r\n                            <div class="navbar-header">\r\n                                <a href="/" title="OpiAnalytics"><img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/mountain.png" id="site_img"/></a>\r\n                            </div>\r\n                            <ul class="nav navbar-nav">\r\n                                <li class="nav-item"><a class="nav-link-')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('" href="/">Home</a></li>\r\n                                <li class="nav-item"><a class="nav-link-')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'catalog' else '' ))
        __M_writer('" href="/catalog/index/">Catalog</a></li>\r\n                                <li class="nav-item"><a class="nav-link-')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('" href="/about/">About</a></li>\r\n')
        if request.user.is_authenticated:
            __M_writer('                                    ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
                context['self'].navbar_items(**pageargs)
            

            __M_writer('\r\n')
        else:
            __M_writer('                                    ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'login_navbar'):
                context['self'].login_navbar(**pageargs)
            

            __M_writer('\r\n')
        __M_writer('                            </ul>\r\n                        </nav>\r\n                            \r\n                        </div>\r\n                       \r\n        </header>\r\n\r\n        <main>\r\n            <div id="site_left">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            \r\n        </main>\r\n\r\n        <footer class="page-footer">\r\n            &copy;Copyright 2019. All rights reserved.\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_maintenance(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_maintenance():
            return render_header_maintenance(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_items():
            return render_navbar_items(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def login_navbar():
            return render_login_navbar(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer("\r\n                Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n                ")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Caleb/OneDrive - BYU Office 365/BYU/Winter19/413/INTEX/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "38": 2, "43": 7, "44": 11, "45": 11, "46": 11, "47": 12, "48": 12, "49": 13, "50": 13, "51": 14, "52": 14, "53": 16, "54": 17, "55": 17, "60": 21, "61": 28, "62": 28, "63": 31, "64": 31, "65": 32, "66": 32, "67": 33, "68": 33, "69": 34, "70": 35, "75": 35, "76": 36, "77": 37, "82": 37, "83": 39, "88": 50, "93": 54, "99": 7, "110": 21, "121": 35, "132": 37, "143": 48, "149": 48, "155": 53, "161": 53, "167": 161}}
__M_END_METADATA
"""
