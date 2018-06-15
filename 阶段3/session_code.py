#!/usr/bin/env python
#encoding:utf-8
import hashlib
import time
import settings
def gen_random_str():
    md5=hashlib.md5()
    md5.update(str(time.time()).encode('utf-8'))
    return md5.hexdigest()

class RedisSession(object):
    container={}
    def __init__(self,handler):
        self.handler=handler
        self.session_id=settings.SESSION_ID
        self.expires=settings.EXPIRES
        self.initial()

    @property
    def conn(self):
        import redis
        pool = redis.ConnectionPool(host='192.168.1.168', port=6379)
        conn = redis.Redis(connection_pool=pool)
        return conn

    def initial(self):
        client_random_str=self.handler.get_cookie(self.session_id)

        if client_random_str and self.conn.exists(client_random_str):
            self.random_str=client_random_str
        else:
            self.random_str=gen_random_str()

        expires=time.time()+self.expires
        self.handler.set_cookie(self.session_id,self.random_str,expires=expires)
        self.conn.expire(self.random_str,self.expires)


    def __getitem__(self, item):
        import json
        data_str= str(self.conn.hget(self.random_str,item),encoding='utf-8')
        if data_str:
            return json.loads(data_str)
        else:
            return None

    def __setitem__(self, key, value):
        import json

        self.conn.hset(self.random_str,key,json.dumps(value))

    def __delitem__(self, key):
        self.conn.hdel(self.random_str,key)


class CacheSession(object):
    container={}
    def __init__(self,handler):
        self.handler=handler
        self.session_id=settings.SESSION_ID
        self.expires=settings.EXPIRES
        self.initial()

    def initial(self):
        client_random_str=self.handler.get_cookie(self.session_id)

        if client_random_str and client_random_str in self.container:
            self.random_str=client_random_str
        else:
            self.random_str=gen_random_str()
            self.container[self.random_str]={}
        expires=time.time()+self.expires
        self.handler.set_cookie(self.session_id,self.random_str,expires=expires)


    def __getitem__(self, item):
        return self.container.get(self.random_str).get(item)

    def __setitem__(self, key, value):
        self.container[self.random_str][key]=value

    def __delitem__(self, key):
        if key in self.container[self.random_str]:
            del self.container[self.random_str][key]

class SessionFactory(object):

    @staticmethod
    def get_session():
        import importlib
        import settings
        path=settings.SESSION_ENGINE
        module_path,cls=path.rsplit('.',maxsplit=1)
        md=importlib.import_module(module_path)
        cls=getattr(md,cls)
        return cls

