#!/usr/bin/env python
#encoding:utf-8
from tornado.web import RequestHandler
class TestHander(RequestHandler):
    def get(self,*args, **kwargs):
        self.render('test.html')

    def post(self, *args, **kwargs):
        file_metas = self.request.files['fff']

        for meta in file_metas:
            file_name = meta['filename']
            with open(file_name, 'wb') as up:
                up.write(meta['body'])

        self.write('ok')