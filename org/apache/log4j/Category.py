def getInstance():
    '''    public static Category getInstance(final String name)
    public static Category getInstance(final Class clazz)
    '''
def getName():
    '''    public final String getName()
    '''
def getParent():
    '''    public final Category getParent()
    '''
def getRoot():
    '''    public static Category getRoot()
    '''
def getCurrentCategories():
    '''    public static Enumeration getCurrentCategories()
    '''
def getEffectiveLevel():
    '''    public final Level getEffectiveLevel()
    '''
def getChainedPriority():
    '''    public final Priority getChainedPriority()
    '''
def getLevel():
    '''    public final Level getLevel()
    '''
def setLevel():
    '''    public void setLevel(final Level level)
    '''
def getPriority():
    '''    public final Level getPriority()
    '''
def setPriority():
    '''    public void setPriority(final Priority priority)
    '''
def debug():
    '''    public void debug(final Object message)
    public void debug(final Object message, final Throwable t)
    '''
def isDebugEnabled():
    '''    public boolean isDebugEnabled()
    '''
def error():
    '''    public void error(final Object message)
    public void error(final Object message, final Throwable t)
    '''
def isErrorEnabled():
    '''    public boolean isErrorEnabled()
    '''
def warn():
    '''    public void warn(final Object message)
    public void warn(final Object message, final Throwable t)
    '''
def isWarnEnabled():
    '''    public boolean isWarnEnabled()
    '''
def fatal():
    '''    public void fatal(final Object message)
    public void fatal(final Object message, final Throwable t)
    '''
def isFatalEnabled():
    '''    public boolean isFatalEnabled()
    '''
def info():
    '''    public void info(final Object message)
    public void info(final Object message, final Throwable t)
    '''
def isInfoEnabled():
    '''    public boolean isInfoEnabled()
    '''
def trace():
    '''    public void trace(final Object message)
    public void trace(final Object message, final Throwable t)
    '''
def isTraceEnabled():
    '''    public boolean isTraceEnabled()
    '''
def isEnabledFor():
    '''    public boolean isEnabledFor(final Priority level)
    '''
def addAppender():
    '''    public void addAppender(final Appender appender)
    '''
def callAppenders():
    '''    public void callAppenders(final LoggingEvent event)
    '''
def getAllAppenders():
    '''    public Enumeration getAllAppenders()
    '''
def getAppender():
    '''    public Appender getAppender(final String name)
    '''
def isAttached():
    '''    public boolean isAttached(final Appender appender)
    '''
def removeAllAppenders():
    '''    public void removeAllAppenders()
    '''
def removeAppender():
    '''    public void removeAppender(final Appender appender)
    public void removeAppender(final String name)
    '''
def shutdown():
    '''    public static void shutdown()
    '''
def forcedLog():
    '''    public void forcedLog(final String fqcn, final Priority level, final Object message, final Throwable t)
    '''
def exists():
    '''    public boolean exists(final String name)
    '''
def getAdditivity():
    '''    public boolean getAdditivity()
    '''
def setAdditivity():
    '''    public void setAdditivity(final boolean additivity)
    '''
def setResourceBundle():
    '''    public void setResourceBundle(final ResourceBundle bundle)
    '''
def getResourceBundle():
    '''    public ResourceBundle getResourceBundle()
    '''
def assertLog():
    '''    public void assertLog(final boolean assertion, final String msg)
    '''
def l7dlog():
    '''    public void l7dlog(final Priority priority, final String key, final Throwable t)
    public void l7dlog(final Priority priority, final String key, final Object[] params, final Throwable t)
    '''
def log():
    '''    public void log(final Priority priority, final Object message, final Throwable t)
    public void log(final Priority priority, final Object message)
    public void log(final String fqcn, final Priority priority, final Object message, final Throwable t)
    '''
def getContext():
    '''    public static LoggerContext getContext()
    '''
