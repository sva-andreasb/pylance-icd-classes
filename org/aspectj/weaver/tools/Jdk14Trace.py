def ():
    '''returns Jdk14Trace\n\n
    (final Class clazz)\n
    '''
def enter():
    '''returns None\n\n
    enter(final String methodName, final Object thiz, final Object[] args)\n
    enter(final String methodName, final Object thiz)\n
    '''
def exit():
    '''returns None\n\n
    exit(final String methodName, final Object ret)\n
    exit(final String methodName, final Throwable th)\n
    exit(final String methodName)\n
    '''
def event():
    '''returns None\n\n
    event(final String methodName, final Object thiz, final Object[] args)\n
    event(final String methodName)\n
    '''
def isTraceEnabled():
    '''returns boolean\n\n
    isTraceEnabled()\n
    '''
def setTraceEnabled():
    '''returns None\n\n
    setTraceEnabled(final boolean b)\n
    '''
def debug():
    '''returns None\n\n
    debug(final String message)\n
    '''
def info():
    '''returns None\n\n
    info(final String message)\n
    '''
def warn():
    '''returns None\n\n
    warn(final String message, final Throwable th)\n
    '''
def error():
    '''returns None\n\n
    error(final String message, final Throwable th)\n
    '''
def fatal():
    '''returns None\n\n
    fatal(final String message, final Throwable th)\n
    '''
