#!/usr/bin/env python
#encoding:utf-8
class RedisSession(object):
    def __getitem__(self, item):
        return item
    def __setitem__(self, key, value):
        pass
    def __delitem__(self, key):
        pass

class CacheSession(object):
    def __getitem__(self, item):
        return item

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

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

