#!/usr/bin/env python
#encoding:utf-8
from tornado.web import RequestHandler
from tornado.web import authenticated
#单继承
"""
class S4RequestHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('nnnnnn')
class SeedHander(S4RequestHandler):
    @authenticated
    def get(self, *args, **kwargs):
        seed_list=[
            {'title':'小麦','price':2},
            {'title':'大麦','price':21},
            {'title':'大桥','price':22},
        ]
        self.render('seed.html',seed_list=seed_list)
"""

#多继承
class S4RequestHandler(object):
    def get_current_user(self):
        return self.get_secure_cookie('nnnnnn')

class SeedHander(S4RequestHandler,RequestHandler):
    @authenticated
    def get(self, *args, **kwargs):
        seed_list=[
            {'title':'小麦','price':2},
            {'title':'大麦','price':21},
            {'title':'大桥','price':22},
        ]
        self.render('seed.html',seed_list=seed_list)