#!/usr/bin/env python
#encoding:utf-8
from session_code import SessionFactory
cls=SessionFactory.get_session()
print(cls)