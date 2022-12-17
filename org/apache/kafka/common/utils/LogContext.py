def ():
    '''returns LogContext\n\n
    (final String logPrefix)\n
    ()\n
    '''
def logger():
    '''returns Logger\n\n
    logger(final Class<?> clazz)\n
    '''
def logPrefix():
    '''returns String\n\n
    logPrefix()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    getName()\n
    '''
def isTraceEnabled():
    '''returns boolean\n\n
    isTraceEnabled()\n
    isTraceEnabled(final Marker marker)\n
    isTraceEnabled()\n
    isTraceEnabled(final Marker marker)\n
    '''
def isDebugEnabled():
    '''returns boolean\n\n
    isDebugEnabled()\n
    isDebugEnabled(final Marker marker)\n
    isDebugEnabled()\n
    isDebugEnabled(final Marker marker)\n
    '''
def isInfoEnabled():
    '''returns boolean\n\n
    isInfoEnabled()\n
    isInfoEnabled(final Marker marker)\n
    isInfoEnabled()\n
    isInfoEnabled(final Marker marker)\n
    '''
def isWarnEnabled():
    '''returns boolean\n\n
    isWarnEnabled()\n
    isWarnEnabled(final Marker marker)\n
    isWarnEnabled()\n
    isWarnEnabled(final Marker marker)\n
    '''
def isErrorEnabled():
    '''returns boolean\n\n
    isErrorEnabled()\n
    isErrorEnabled(final Marker marker)\n
    isErrorEnabled()\n
    isErrorEnabled(final Marker marker)\n
    '''
def trace():
    '''returns None\n\n
    trace(final String message)\n
    trace(final String format, final Object arg)\n
    trace(final String format, final Object arg1, final Object arg2)\n
    trace(final String format, final Object... args)\n
    trace(final String msg, final Throwable t)\n
    trace(final Marker marker, final String msg)\n
    trace(final Marker marker, final String format, final Object arg)\n
    trace(final Marker marker, final String format, final Object arg1, final Object arg2)\n
    trace(final Marker marker, final String format, final Object... argArray)\n
    trace(final Marker marker, final String msg, final Throwable t)\n
    trace(final String message)\n
    trace(final String message, final Object arg)\n
    trace(final String message, final Object arg1, final Object arg2)\n
    trace(final String message, final Object... args)\n
    trace(final String msg, final Throwable t)\n
    trace(final Marker marker, final String msg)\n
    trace(final Marker marker, final String format, final Object arg)\n
    trace(final Marker marker, final String format, final Object arg1, final Object arg2)\n
    trace(final Marker marker, final String format, final Object... argArray)\n
    trace(final Marker marker, final String msg, final Throwable t)\n
    '''
def debug():
    '''returns None\n\n
    debug(final String message)\n
    debug(final String format, final Object arg)\n
    debug(final String format, final Object arg1, final Object arg2)\n
    debug(final String format, final Object... args)\n
    debug(final String msg, final Throwable t)\n
    debug(final Marker marker, final String msg)\n
    debug(final Marker marker, final String format, final Object arg)\n
    debug(final Marker marker, final String format, final Object arg1, final Object arg2)\n
    debug(final Marker marker, final String format, final Object... arguments)\n
    debug(final Marker marker, final String msg, final Throwable t)\n
    debug(final String message)\n
    debug(final String message, final Object arg)\n
    debug(final String message, final Object arg1, final Object arg2)\n
    debug(final String message, final Object... args)\n
    debug(final String msg, final Throwable t)\n
    debug(final Marker marker, final String msg)\n
    debug(final Marker marker, final String format, final Object arg)\n
    debug(final Marker marker, final String format, final Object arg1, final Object arg2)\n
    debug(final Marker marker, final String format, final Object... arguments)\n
    debug(final Marker marker, final String msg, final Throwable t)\n
    '''
def warn():
    '''returns None\n\n
    warn(final String message)\n
    warn(final String format, final Object arg)\n
    warn(final String message, final Object arg1, final Object arg2)\n
    warn(final String format, final Object... args)\n
    warn(final String msg, final Throwable t)\n
    warn(final Marker marker, final String msg)\n
    warn(final Marker marker, final String format, final Object arg)\n
    warn(final Marker marker, final String format, final Object arg1, final Object arg2)\n
    warn(final Marker marker, final String format, final Object... arguments)\n
    warn(final Marker marker, final String msg, final Throwable t)\n
    warn(final String message)\n
    warn(final String message, final Object arg)\n
    warn(final String message, final Object arg1, final Object arg2)\n
    warn(final String message, final Object... args)\n
    warn(final String msg, final Throwable t)\n
    warn(final Marker marker, final String msg)\n
    warn(final Marker marker, final String format, final Object arg)\n
    warn(final Marker marker, final String format, final Object arg1, final Object arg2)\n
    warn(final Marker marker, final String format, final Object... arguments)\n
    warn(final Marker marker, final String msg, final Throwable t)\n
    '''
def error():
    '''returns None\n\n
    error(final String message)\n
    error(final String format, final Object arg)\n
    error(final String format, final Object arg1, final Object arg2)\n
    error(final String format, final Object... args)\n
    error(final String msg, final Throwable t)\n
    error(final Marker marker, final String msg)\n
    error(final Marker marker, final String format, final Object arg)\n
    error(final Marker marker, final String format, final Object arg1, final Object arg2)\n
    error(final Marker marker, final String format, final Object... arguments)\n
    error(final Marker marker, final String msg, final Throwable t)\n
    error(final String message)\n
    error(final String message, final Object arg)\n
    error(final String message, final Object arg1, final Object arg2)\n
    error(final String message, final Object... args)\n
    error(final String msg, final Throwable t)\n
    error(final Marker marker, final String msg)\n
    error(final Marker marker, final String format, final Object arg)\n
    error(final Marker marker, final String format, final Object arg1, final Object arg2)\n
    error(final Marker marker, final String format, final Object... arguments)\n
    error(final Marker marker, final String msg, final Throwable t)\n
    '''
def info():
    '''returns None\n\n
    info(final String msg)\n
    info(final String format, final Object arg)\n
    info(final String format, final Object arg1, final Object arg2)\n
    info(final String format, final Object... args)\n
    info(final String msg, final Throwable t)\n
    info(final Marker marker, final String msg)\n
    info(final Marker marker, final String format, final Object arg)\n
    info(final Marker marker, final String format, final Object arg1, final Object arg2)\n
    info(final Marker marker, final String format, final Object... arguments)\n
    info(final Marker marker, final String msg, final Throwable t)\n
    info(final String message)\n
    info(final String message, final Object arg)\n
    info(final String message, final Object arg1, final Object arg2)\n
    info(final String message, final Object... args)\n
    info(final String msg, final Throwable t)\n
    info(final Marker marker, final String msg)\n
    info(final Marker marker, final String format, final Object arg)\n
    info(final Marker marker, final String format, final Object arg1, final Object arg2)\n
    info(final Marker marker, final String format, final Object... arguments)\n
    info(final Marker marker, final String msg, final Throwable t)\n
    '''
