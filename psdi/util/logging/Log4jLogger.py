def Log4jLogger():
    '''public Log4jLogger(final String name)
    public Log4jLogger(final String name, final ResourceBundle resourceBundle)
    '''
def debug():
    '''public void debug(Object message)
    public void debug(Object message, final Throwable t)
    '''
def info():
    '''public void info(Object message)
    public void info(Object message, final Throwable t)
    '''
def warn():
    '''public void warn(Object message)
    public void warn(Object message, final Throwable t)
    '''
def error():
    '''public void error(Object message)
    public void error(Object message, final Throwable t)
    '''
def fatal():
    '''public void fatal(Object message)
    public void fatal(Object message, final Throwable t)
    '''
def isDebugEnabled():
    '''public boolean isDebugEnabled()
    '''
def isErrorEnabled():
    '''public boolean isErrorEnabled()
    '''
def isFatalEnabled():
    '''public boolean isFatalEnabled()
    '''
def isInfoEnabled():
    '''public boolean isInfoEnabled()
    '''
def isTraceEnabled():
    '''public boolean isTraceEnabled()
    '''
def isWarnEnabled():
    '''public boolean isWarnEnabled()
    '''
def setLevel():
    '''public void setLevel(final Level level)
    '''
def getLevel():
    '''public Level getLevel()
    '''
def logDisregardLevel():
    '''public void logDisregardLevel(final String msgGroup, final String msgKey, final Object[] params)
    '''
def addAppender():
    '''public void addAppender(final Appender newAppender)
    '''
def removeAppender():
    '''public void removeAppender(final String name)
    '''
def getAppender():
    '''public Appender getAppender(final String name)
    '''
