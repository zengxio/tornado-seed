#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web

from Tyrion.Forms import Form
from Tyrion.Fields import StringField
from Tyrion.Fields import EmailField


class LoginForm(Form):
    username = StringField(error={'required': '用户名不能为空'})
    password = StringField(error={'required': '密码不能为空'})
    email = EmailField(error={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'})


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        form = LoginForm(self)
        self.render('login.html', form=form)

    def post(self, *args, **kwargs):
        form = LoginForm(self)

        # 检查用户输入是否合法
        if form.is_valid():
            print('合法，用户输入内容:', form.value_dict)
        else:
            # 如果不合法，则输出错误信息
            print('不合法, 错误信息:', form.error_dict)
        self.render('login.html', form=form)


application = tornado.web.Application([

    (r"/login.html", LoginHandler),
])

if __name__ == "__main__":
    import Tyrion
    Tyrion.setup('tornado')

    print('http://127.0.0.1:8888')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()