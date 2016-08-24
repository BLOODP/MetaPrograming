import logging
from functools import wraps

def logged(level,name=None,message=None):

    def decorate(func):
        logname = name if name else func.__module__
        print('logname: ',logname)
        log = logging.getLogger(name)
        logmsg = message if message else func.__name__
        print('logmsg : ',logmsg)

        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logmsg)
            return func(*args,**kwargs)
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x,y):
    return x+y

@logged(logging.CRITICAL,'example')
def spam():
    print('Spam')

print('re:',add(2,4))
spam()