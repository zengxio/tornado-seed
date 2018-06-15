#!/usr/bin/env python
#encoding:utf-8
#定制session组件
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
from session_code import SessionFactory
class SessionHandler(object):
    def initialize(self,*args,**kwargs):
        cls = SessionFactory.get_session()
        self.session = cls(self)

class LoginHandler(SessionHandler,RequestHandler):

    def get(self):
        self.render('login.html')

    def post(self, *args, **kwargs):
        user=self.get_argument('user')
        pwd=self.get_argument('pwd')
        if user=='alex' and pwd=='123':
            self.session['user']=user
            self.redirect('/index')
        else:
            self.render('login.html')

class IndexHandler(SessionHandler,RequestHandler):
    def get(self,*args,**kwargs):
        user=self.session['user']
        if user:
            self.write('欢迎登录')
        else:
            self.redirect('/login')

sett={
    'template_path':'views'
}
application = tornado.web.Application([
    (r"/login", LoginHandler),
    (r"/index", IndexHandler)
],**sett)


if __name__ == "__main__":
    application.listen(9999) #监听8888端口
    tornado.ioloop.IOLoop.instance().start() #启动程序