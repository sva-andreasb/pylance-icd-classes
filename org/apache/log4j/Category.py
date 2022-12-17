def setLevel():
    '''returns None\n\n
    setLevel(final Level level)\n
    '''
def setPriority():
    '''returns None\n\n
    setPriority(final Priority priority)\n
    '''
def debug():
    '''returns None\n\n
    debug(final Object message)\n
    debug(final Object message, final Throwable t)\n
    '''
def isDebugEnabled():
    '''returns boolean\n\n
    isDebugEnabled()\n
    '''
def error():
    '''returns None\n\n
    error(final Object message)\n
    error(final Object message, final Throwable t)\n
    '''
def isErrorEnabled():
    '''returns boolean\n\n
    isErrorEnabled()\n
    '''
def warn():
    '''returns None\n\n
    warn(final Object message)\n
    warn(final Object message, final Throwable t)\n
    '''
def isWarnEnabled():
    '''returns boolean\n\n
    isWarnEnabled()\n
    '''
def fatal():
    '''returns None\n\n
    fatal(final Object message)\n
    fatal(final Object message, final Throwable t)\n
    '''
def isFatalEnabled():
    '''returns boolean\n\n
    isFatalEnabled()\n
    '''
def info():
    '''returns None\n\n
    info(final Object message)\n
    info(final Object message, final Throwable t)\n
    '''
def isInfoEnabled():
    '''returns boolean\n\n
    isInfoEnabled()\n
    '''
def trace():
    '''returns None\n\n
    trace(final Object message)\n
    trace(final Object message, final Throwable t)\n
    '''
def isTraceEnabled():
    '''returns boolean\n\n
    isTraceEnabled()\n
    '''
def isEnabledFor():
    '''returns boolean\n\n
    isEnabledFor(final Priority level)\n
    '''
def addAppender():
    '''returns None\n\n
    addAppender(final Appender appender)\n
    '''
def callAppenders():
    '''returns None\n\n
    callAppenders(final LoggingEvent event)\n
    '''
def getAllAppenders():
    '''returns Enumeration\n\n
    getAllAppenders()\n
    '''
def getAppender():
    '''returns Appender\n\n
    getAppender(final String name)\n
    '''
def isAttached():
    '''returns boolean\n\n
    isAttached(final Appender appender)\n
    '''
def removeAllAppenders():
    '''returns None\n\n
    removeAllAppenders()\n
    '''
def removeAppender():
    '''returns None\n\n
    removeAppender(final Appender appender)\n
    removeAppender(final String name)\n
    '''
def forcedLog():
    '''returns None\n\n
    forcedLog(final String fqcn, final Priority level, final Object message, final Throwable t)\n
    '''
def exists():
    '''returns boolean\n\n
    exists(final String name)\n
    '''
def getAdditivity():
    '''returns boolean\n\n
    getAdditivity()\n
    '''
def setAdditivity():
    '''returns None\n\n
    setAdditivity(final boolean additivity)\n
    '''
def setResourceBundle():
    '''returns None\n\n
    setResourceBundle(final ResourceBundle bundle)\n
    '''
def getResourceBundle():
    '''returns ResourceBundle\n\n
    getResourceBundle()\n
    '''
def assertLog():
    '''returns None\n\n
    assertLog(final boolean assertion, final String msg)\n
    '''
def l7dlog():
    '''returns None\n\n
    l7dlog(final Priority priority, final String key, final Throwable t)\n
    l7dlog(final Priority priority, final String key, final Object[] params, final Throwable t)\n
    '''
def log():
    '''returns None\n\n
    log(final Priority priority, final Object message, final Throwable t)\n
    log(final Priority priority, final Object message)\n
    log(final String fqcn, final Priority priority, final Object message, final Throwable t)\n
    '''
