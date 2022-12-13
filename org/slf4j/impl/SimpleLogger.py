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
    '''    public boolean isTraceEnabled()
    '''
def trace():
    '''    public void trace(final String msg)
    public void trace(final String format, final Object param1)
    public void trace(final String format, final Object param1, final Object param2)
    public void trace(final String format, final Object... argArray)
    public void trace(final String msg, final Throwable t)
    '''
def isDebugEnabled():
    '''    public boolean isDebugEnabled()
    '''
def debug():
    '''    public void debug(final String msg)
    public void debug(final String format, final Object param1)
    public void debug(final String format, final Object param1, final Object param2)
    public void debug(final String format, final Object... argArray)
    public void debug(final String msg, final Throwable t)
    '''
def isInfoEnabled():
    '''    public boolean isInfoEnabled()
    '''
def info():
    '''    public void info(final String msg)
    public void info(final String format, final Object arg)
    public void info(final String format, final Object arg1, final Object arg2)
    public void info(final String format, final Object... argArray)
    public void info(final String msg, final Throwable t)
    '''
def isWarnEnabled():
    '''    public boolean isWarnEnabled()
    '''
def warn():
    '''    public void warn(final String msg)
    public void warn(final String format, final Object arg)
    public void warn(final String format, final Object arg1, final Object arg2)
    public void warn(final String format, final Object... argArray)
    public void warn(final String msg, final Throwable t)
    '''
def isErrorEnabled():
    '''    public boolean isErrorEnabled()
    '''
def error():
    '''    public void error(final String msg)
    public void error(final String format, final Object arg)
    public void error(final String format, final Object arg1, final Object arg2)
    public void error(final String format, final Object... argArray)
    public void error(final String msg, final Throwable t)
    '''
def log():
    '''    public void log(final LoggingEvent event)
    '''
