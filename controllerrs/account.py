#!/usr/bin/env python
#encoding:utf-8
from tornado.web import RequestHandler

class LoginHander(RequestHandler):

    def get(self, *args, **kwargs):
        # self.write("get") #字符串返回
        self.render('login.html',msg='')

    def post(self, *args, **kwargs):
        # print(self.get_body_argument('user')) #获取post数据
        # print(self.get_body_arguments('user')) #获取post多个数据
        # print(self.get_query_argument('id')) #获取get数据
        # self.get_query_arguments('id') #获取get多个数据

        user=self.get_argument('user')  #post和get都获取
        pwd=self.get_argument('pwd')
        if user=='alex' and pwd=='123':
            import time
            v=time.time()+300
            # self.set_cookie('nnnnnn',user,expires=v) #设置为10秒钟后失效
            self.set_secure_cookie('nnnnnn',user,expires=v)
            next_url=self.get_query_argument('next')
            if not next_url:
                next_url='/seed.html'
            self.redirect(next_url)
        else:
            self.render('login.html',msg='用户名或密码错误')
