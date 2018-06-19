#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
from Web.Controllers import Demo


settings = {
    'template_path': 'Web/Views'
}

application = tornado.web.Application([
    (r"/index.html", Demo.IndexHandler),
    (r"/login.html", Demo.LoginHandler),
    (r"/register.html", Demo.RegisterHandler),
    (r"/multi_checkbox.html", Demo.MultiCheckBoxHandler),
    (r"/multi_select.html", Demo.MultiSelectHandler),
    (r"/dynamic_select.html", Demo.DynamicSelectHandler),
    (r"/init_value.html", Demo.InitValueHandler),
], **settings)

if __name__ == "__main__":

    ###########################
    # pip3 install PyTyrion
    # site-package, Tyrion
    import Tyrion
    Tyrion.setup('tornado')
    # 配置，当前组件支持什么WEB框架：Django、Bottle、Flask、Tornado
    ###########################

    print('http://127.0.0.1:8888')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()