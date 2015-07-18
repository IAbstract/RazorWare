"""
"""
__author__ = 'David Boarman, RazorWare, LLC'

from functools import wraps

from .dynamic_router import DynamicRouter

THREAD_LOCAL = DynamicRouter.thread_local


class DataContext(object):
    """DataContext allows routing to a database using a database name
    """
    def __init__(self, database, read=True, write=False):
        self.read = read
        self.write = write
        self.created_db_config = False
        self.database = database

    def __enter__(self):
        if self.read:
            setattr(THREAD_LOCAL, 'DB_FOR_READ_OVERRIDE', self.database)
        if self.write:
            setattr(THREAD_LOCAL, 'DB_FOR_WRITE_OVERRIDE', self.database)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        setattr(THREAD_LOCAL, 'DB_FOR_READ_OVERRIDE', None)
        setattr(THREAD_LOCAL, 'DB_FOR_WRITE_OVERRIDE', None)

    def __call__(self, querying_func):
        @wraps(querying_func)
        def inner(*args, **kwargs):
            # Call the function in our context manager
            with self:
                return querying_func(*args, **kwargs)
        return inner