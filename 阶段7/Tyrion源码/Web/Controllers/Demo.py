#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from Web.Forms.Demo import LoginForm
from Web.Forms.Demo import RegisterForm
from Web.Forms.Demo import MultiCheckBoxForm
from Web.Forms.Demo import MultiSelectForm
from Web.Forms.Demo import DynamicSelectForm
from Web.Forms.Demo import InitValueForm


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        form = LoginForm(self)
        self.render('login.html', form=form)

    def post(self, *args, **kwargs):
        form = LoginForm(self)
        print(form.is_valid())
        print(form.error_dict)
        print(form.value_dict)

        self.render('login.html', form=form)


class RegisterHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        form = RegisterForm(self)
        self.render('register.html', form=form)

    def post(self, *args, **kwargs):
        form = RegisterForm(self)
        print(form.is_valid())
        print('error_dict===>', form.error_dict)
        print('value_dict===>', form.value_dict)

        self.render('register.html', form=form)


class MultiCheckBoxHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        form = MultiCheckBoxForm(self)
        self.render('multi_checkbox.html', form=form)

    def post(self, *args, **kwargs):
        form = MultiCheckBoxForm(self)
        print(form.is_valid())
        print('error_dict===>', form.error_dict)
        print('value_dict===>', form.value_dict)

        self.render('multi_checkbox.html', form=form)


class MultiSelectHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        form = MultiSelectForm(self)
        self.render('multi_select.html', form=form)

    def post(self, *args, **kwargs):
        form = MultiSelectForm(self)
        print(form.is_valid())
        print('error_dict===>', form.error_dict)
        print('value_dict===>', form.value_dict)

        self.render('multi_select.html', form=form)


class DynamicSelectHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        form = DynamicSelectForm(self)
        self.render('dynamic_select.html', form=form)

    def post(self, *args, **kwargs):
        form = DynamicSelectForm(self)
        print(form.is_valid())
        print('error_dict===>', form.error_dict)
        print('value_dict===>', form.value_dict)

        self.render('dynamic_select.html', form=form)


class InitValueHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        form = InitValueForm(self)
        init_dict = {
            'username': 'seven',
            'age': 18,
            'city': 2,
            'gender': 2,
            'protocol': 1,
            'favor_int_val': [1, 3],
            'favor_str_val': ['1', '3'],
            'select_int_val': [1, 3],
            'select_str_val': ['1', '3']

        }
        form.init_field_value(init_dict)

        self.render('init_value.html', form=form)

    def post(self, *args, **kwargs):
        form = InitValueForm(self)
        print(form.is_valid())
        print('error_dict===>', form.error_dict)
        print('value_dict===>', form.value_dict)

        self.render('init_value.html', form=form)

