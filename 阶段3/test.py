#!/usr/bin/env python
#encoding:utf-8
import redis

pool = redis.ConnectionPool(host='192.168.1.168', port=6379)
conn = redis.Redis(connection_pool=pool)
# conn.hset('dfjiasojfdasjdsak','is_login','true')
# conn.expire('dfjiasojfdasjdsak',5)
v=conn.hget('dfjiasojfdasjdsak','is_login')
print(v)