#!/usr/bin/env python
#encoding:utf-8
import tornado.ioloop
import tornado.web #tornado.web.RequestHandler引用
from tornado.web import RequestHandler
"""
session和cookie的关系
cookie: 浏览器上的键值对
session: 保存在服务器端的键值对
"""

class IndexHandler(RequestHandler):
    def get(self):
        url1=self.application.reverse_url('t1')
        url2=self.application.reverse_url('t2',666)
        # application #self.application 代表application
        print(url1,url2) #/test /test_path/666
        self.write("Hello, world")

class DomainHandler(RequestHandler):
    def get(self,nid): #接收参数 也可以改成*args,**kwargs接收多个参数
        print(nid)
        self.write('Hello oldman')

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/test", IndexHandler,{},"t1"),
    (r"/test_path/(\d+)", DomainHandler,{},"t2"),
    (r"/home/(\d+)", DomainHandler), #匹配正则表达式
])

# application.add_handlers('www.domain.com',[(r"/home/(\d+)", DomainHandler)])
# #优先匹配域名,如果匹配不上，在走默认的



if __name__ == "__main__":
    application.listen(8888) #监听8888端口
    tornado.ioloop.IOLoop.instance().start() #启动程序