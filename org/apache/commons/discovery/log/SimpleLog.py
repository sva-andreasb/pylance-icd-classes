LOG_LEVEL_TRACE = "int  1"
LOG_LEVEL_DEBUG = "int  2"
LOG_LEVEL_INFO = "int  3"
LOG_LEVEL_WARN = "int  4"
LOG_LEVEL_ERROR = "int  5"
LOG_LEVEL_FATAL = "int  6"
LOG_LEVEL_ALL = "int  0"
LOG_LEVEL_OFF = "int  7"
def setLevel():
    '''public static void setLevel(final int currentLogLevel)
    '''
def getLevel():
    '''public static int getLevel()
    '''
def SimpleLog():
    '''public SimpleLog(final String name)
    '''
def debug():
    '''public final void debug(final Object message)
    public final void debug(final Object message, final Throwable t)
    '''
def trace():
    '''public final void trace(final Object message)
    public final void trace(final Object message, final Throwable t)
    '''
def info():
    '''public final void info(final Object message)
    public final void info(final Object message, final Throwable t)
    '''
def warn():
    '''public final void warn(final Object message)
    public final void warn(final Object message, final Throwable t)
    '''
def error():
    '''public final void error(final Object message)
    public final void error(final Object message, final Throwable t)
    '''
def fatal():
    '''public final void fatal(final Object message)
    public final void fatal(final Object message, final Throwable t)
    '''
def isDebugEnabled():
    '''public final boolean isDebugEnabled()
    '''
def isErrorEnabled():
    '''public final boolean isErrorEnabled()
    '''
def isFatalEnabled():
    '''public final boolean isFatalEnabled()
    '''
def isInfoEnabled():
    '''public final boolean isInfoEnabled()
    '''
def isTraceEnabled():
    '''public final boolean isTraceEnabled()
    '''
def isWarnEnabled():
    '''public final boolean isWarnEnabled()
    '''
