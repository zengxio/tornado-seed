#!/usr/bin/env python
#encoding:utf-8
import tornado.ioloop
import tornado.web
from controllerrs.account import LoginHander
from controllerrs.seed import SeedHander
settings={
    'template_path':'views',
    'static_path':'ssssss',
    'static_url_prefix':'/static/',
    'xsrf_cookiew':True,
    'cookie_secret':'fjdklsajfowje',
    'login_url':'/login.html'
}
application = tornado.web.Application([
    (r"/login.html", LoginHander),
    (r"/seed.html", SeedHander),

],**settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()