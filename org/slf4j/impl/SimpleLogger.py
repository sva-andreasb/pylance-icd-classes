SYSTEM_PREFIX = "String  \"org.slf4j.simpleLogger.\""
LOG_KEY_PREFIX = "String  \"org.slf4j.simpleLogger.log.\""
CACHE_OUTPUT_STREAM_STRING_KEY = "String  \"org.slf4j.simpleLogger.cacheOutputStream\""
WARN_LEVEL_STRING_KEY = "String  \"org.slf4j.simpleLogger.warnLevelString\""
LEVEL_IN_BRACKETS_KEY = "String  \"org.slf4j.simpleLogger.levelInBrackets\""
LOG_FILE_KEY = "String  \"org.slf4j.simpleLogger.logFile\""
SHOW_SHORT_LOG_NAME_KEY = "String  \"org.slf4j.simpleLogger.showShortLogName\""
SHOW_LOG_NAME_KEY = "String  \"org.slf4j.simpleLogger.showLogName\""
SHOW_THREAD_NAME_KEY = "String  \"org.slf4j.simpleLogger.showThreadName\""
DATE_TIME_FORMAT_KEY = "String  \"org.slf4j.simpleLogger.dateTimeFormat\""
SHOW_DATE_TIME_KEY = "String  \"org.slf4j.simpleLogger.showDateTime\""
DEFAULT_LOG_LEVEL_KEY = "String  \"org.slf4j.simpleLogger.defaultLogLevel\""
def isTraceEnabled():
    '''returns boolean\n\n
    isTraceEnabled()\n
    '''
def trace():
    '''returns None\n\n
    trace(final String msg)\n
    trace(final String format, final Object param1)\n
    trace(final String format, final Object param1, final Object param2)\n
    trace(final String format, final Object... argArray)\n
    trace(final String msg, final Throwable t)\n
    '''
def isDebugEnabled():
    '''returns boolean\n\n
    isDebugEnabled()\n
    '''
def debug():
    '''returns None\n\n
    debug(final String msg)\n
    debug(final String format, final Object param1)\n
    debug(final String format, final Object param1, final Object param2)\n
    debug(final String format, final Object... argArray)\n
    debug(final String msg, final Throwable t)\n
    '''
def isInfoEnabled():
    '''returns boolean\n\n
    isInfoEnabled()\n
    '''
def info():
    '''returns None\n\n
    info(final String msg)\n
    info(final String format, final Object arg)\n
    info(final String format, final Object arg1, final Object arg2)\n
    info(final String format, final Object... argArray)\n
    info(final String msg, final Throwable t)\n
    '''
def isWarnEnabled():
    '''returns boolean\n\n
    isWarnEnabled()\n
    '''
def warn():
    '''returns None\n\n
    warn(final String msg)\n
    warn(final String format, final Object arg)\n
    warn(final String format, final Object arg1, final Object arg2)\n
    warn(final String format, final Object... argArray)\n
    warn(final String msg, final Throwable t)\n
    '''
def isErrorEnabled():
    '''returns boolean\n\n
    isErrorEnabled()\n
    '''
def error():
    '''returns None\n\n
    error(final String msg)\n
    error(final String format, final Object arg)\n
    error(final String format, final Object arg1, final Object arg2)\n
    error(final String format, final Object... argArray)\n
    error(final String msg, final Throwable t)\n
    '''
def log():
    '''returns None\n\n
    log(final LoggingEvent event)\n
    '''
