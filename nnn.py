#!/usr/bin/env python
#encoding:utf-8
from tornado.web import UIModule
from tornado import escape
class Custom(UIModule):
    def render(self, *args, **kwargs):
        return "this is a test"

    def css_files(self):
        """自动会在前端引用css
        <link href="/css/common.css" type="text/css" rel="stylesheet">
        """
        return ["/css/common.css",]

    def embedded_css(self):
        """嵌入css样式"""
        tpl="""
        .c2{
            color:red
        }
        """
        return tpl

    def javascript_files(self):
        """前端引用该地址的js
        <script src="/js/aaa.js" type="text/javascript"></script>
        """
        return ['/ssssss/js/jquery-1.12.4.js']

    def embedded_javascript(self):
        """嵌入js"""
        tpl="""
        v=123;
        console.log(v)
        """
        return tpl
