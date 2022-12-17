def ():
    '''returns CCILogger\n\n
    (final MXLogger logger)\n
    '''
def isDebug():
    '''returns boolean\n\n
    isDebug()\n
    '''
def isInfo():
    '''returns boolean\n\n
    isInfo()\n
    '''
def isWarn():
    '''returns boolean\n\n
    isWarn()\n
    '''
def isError():
    '''returns boolean\n\n
    isError()\n
    '''
def debug():
    '''returns None\n\n
    debug(final String className, final String method, final String msg)\n
    debug(final String className, final String method, final String msg, final Throwable t)\n
    '''
def info():
    '''returns None\n\n
    info(final String className, final String method, final String msg)\n
    info(final String className, final String method, final String msg, final Throwable t)\n
    '''
def warn():
    '''returns None\n\n
    warn(final String className, final String method, final String msg)\n
    warn(final String className, final String method, final String msg, final Throwable t)\n
    '''
def error():
    '''returns None\n\n
    error(final String className, final String method, final String msg)\n
    error(final String className, final String method, final String msg, final Throwable t)\n
    '''
def fatal():
    '''returns None\n\n
    fatal(final String className, final String method, final String msg)\n
    fatal(final String className, final String method, final String msg, final Throwable t)\n
    '''
def debugEntry():
    '''returns None\n\n
    debugEntry(final String className, final String method, final Object[] params)\n
    debugEntry(final String className, final String method)\n
    debugEntry(final String className, final String method, final Object param1)\n
    debugEntry(final String className, final String method, final Object param1, final Object param2)\n
    debugEntry(final String className, final String method, final Object param1, final Object param2, final Object param3)\n
    debugEntry(final String className, final String method, final Object param1, final Object param2, final Object param3, final Object param4)\n
    '''
def debugExit():
    '''returns None\n\n
    debugExit(final String className, final String method, final Object returnValue)\n
    debugExit(final String className, final String method)\n
    '''
