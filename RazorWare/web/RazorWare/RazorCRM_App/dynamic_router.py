"""
"""
__author__ = 'David Boarman, RazorWare, LLC'

import threading


class DynamicRouter(object):
    """A dynamic data router that requires only the name of the database
    """
    thread_local = threading.local()

    def db_for_read(self, model, **hints):
        return getattr(self.thread_local, 'DB_FOR_READ_OVERRIDE', 'default')

    def db_for_write(self, model, **hints):
        return getattr(self.thread_local, 'DB_FOR_WRITE_OVERRIDE', 'default')

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_syncdb(self, db, model):
        return True

    def allow_migrate(self, db, model):
        return self.allow_syncdb(db, model)