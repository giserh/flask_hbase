#!/usr/bin/env python
# encoding: utf-8

import happybase
import contextlib
from flask import current_app

__all__ = ('FlaskHbase', )
__version__ = '0.1.0'

db_prefix = "HBASE"
#logger = logging.getLogger(__name__)

class FlaskHbase(object):
    config_prefix = db_prefix
    time_out = None

    def __init__(self, app=None, config_prefix=db_prefix):
        if app is not None:
            self.init_app(app, config_prefix)

    def init_app(self, app, config_prefix=db_prefix):
        app.extensions.setdefault('hbase', {})

        self.config_prefix = config_prefix
        self.time_out = app.config.setdefault(self.key('TIME_OUT'), 1000*1000)
        self.host = app.config.setdefault(self.key('HOST'), 'localhost')
        self.port = app.config.setdefault(self.key('PORT'), 9090)
        pool_size = app.config.setdefault(self.key('POOL_SIZE'), 10)
        pool = happybase.ConnectionPool(size=pool_size, host=self.host, port=self.port)
        app.extensions['hbase']['pool'] = pool

    def key(self, suffix):
        return '%s_%s' % (self.config_prefix, suffix)

    @property
    def conn_from_pool(self):
        return current_app.extensions["hbase"]["pool"].connection(timeout=self.time_out)

    @property
    @contextlib.contextmanager
    def connection(self):
        try:
            conn = happybase.Connection(host=self.host, port=self.port, timeout=self.time_out)
            conn.open()
            yield conn
        except Exception as e:
            print str(e)
        finally:
            conn.close()
