def ():
    '''returns Log4jLogger\n\n
    (final String name)\n
    (final String name, final ResourceBundle resourceBundle)\n
    '''
def debug():
    '''returns None\n\n
    debug(Object message)\n
    debug(Object message, final Throwable t)\n
    '''
def info():
    '''returns None\n\n
    info(Object message)\n
    info(Object message, final Throwable t)\n
    '''
def warn():
    '''returns None\n\n
    warn(Object message)\n
    warn(Object message, final Throwable t)\n
    '''
def error():
    '''returns None\n\n
    error(Object message)\n
    error(Object message, final Throwable t)\n
    '''
def fatal():
    '''returns None\n\n
    fatal(Object message)\n
    fatal(Object message, final Throwable t)\n
    '''
def isDebugEnabled():
    '''returns boolean\n\n
    isDebugEnabled()\n
    '''
def isErrorEnabled():
    '''returns boolean\n\n
    isErrorEnabled()\n
    '''
def isFatalEnabled():
    '''returns boolean\n\n
    isFatalEnabled()\n
    '''
def isInfoEnabled():
    '''returns boolean\n\n
    isInfoEnabled()\n
    '''
def isTraceEnabled():
    '''returns boolean\n\n
    isTraceEnabled()\n
    '''
def isWarnEnabled():
    '''returns boolean\n\n
    isWarnEnabled()\n
    '''
def setLevel():
    '''returns None\n\n
    setLevel(final Level level)\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel()\n
    '''
def logDisregardLevel():
    '''returns None\n\n
    logDisregardLevel(final String msgGroup, final String msgKey, final Object[] params)\n
    '''
def addAppender():
    '''returns None\n\n
    addAppender(final Appender newAppender)\n
    '''
def removeAppender():
    '''returns None\n\n
    removeAppender(final String name)\n
    '''
def getAppender():
    '''returns Appender\n\n
    getAppender(final String name)\n
    '''
