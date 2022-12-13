def getInstance():
'''public static Category getInstance(final String name)
public static Category getInstance(final Class clazz)
'''
pass
def getName():
'''public final String getName()
'''
pass
def getParent():
'''public final Category getParent()
'''
pass
def getRoot():
'''public static Category getRoot()
'''
pass
def getCurrentCategories():
'''public static Enumeration getCurrentCategories()
'''
pass
def getEffectiveLevel():
'''public final Level getEffectiveLevel()
'''
pass
def getChainedPriority():
'''public final Priority getChainedPriority()
'''
pass
def getLevel():
'''public final Level getLevel()
'''
pass
def setLevel():
'''public void setLevel(final Level level)
'''
pass
def getPriority():
'''public final Level getPriority()
'''
pass
def setPriority():
'''public void setPriority(final Priority priority)
'''
pass
def debug():
'''public void debug(final Object message)
public void debug(final Object message, final Throwable t)
'''
pass
def isDebugEnabled():
'''public boolean isDebugEnabled()
'''
pass
def error():
'''public void error(final Object message)
public void error(final Object message, final Throwable t)
'''
pass
def isErrorEnabled():
'''public boolean isErrorEnabled()
'''
pass
def warn():
'''public void warn(final Object message)
public void warn(final Object message, final Throwable t)
'''
pass
def isWarnEnabled():
'''public boolean isWarnEnabled()
'''
pass
def fatal():
'''public void fatal(final Object message)
public void fatal(final Object message, final Throwable t)
'''
pass
def isFatalEnabled():
'''public boolean isFatalEnabled()
'''
pass
def info():
'''public void info(final Object message)
public void info(final Object message, final Throwable t)
'''
pass
def isInfoEnabled():
'''public boolean isInfoEnabled()
'''
pass
def trace():
'''public void trace(final Object message)
public void trace(final Object message, final Throwable t)
'''
pass
def isTraceEnabled():
'''public boolean isTraceEnabled()
'''
pass
def isEnabledFor():
'''public boolean isEnabledFor(final Priority level)
'''
pass
def addAppender():
'''public void addAppender(final Appender appender)
'''
pass
def callAppenders():
'''public void callAppenders(final LoggingEvent event)
'''
pass
def getAllAppenders():
'''public Enumeration getAllAppenders()
'''
pass
def getAppender():
'''public Appender getAppender(final String name)
'''
pass
def isAttached():
'''public boolean isAttached(final Appender appender)
'''
pass
def removeAllAppenders():
'''public void removeAllAppenders()
'''
pass
def removeAppender():
'''public void removeAppender(final Appender appender)
public void removeAppender(final String name)
'''
pass
def shutdown():
'''public static void shutdown()
'''
pass
def forcedLog():
'''public void forcedLog(final String fqcn, final Priority level, final Object message, final Throwable t)
'''
pass
def exists():
'''public boolean exists(final String name)
'''
pass
def getAdditivity():
'''public boolean getAdditivity()
'''
pass
def setAdditivity():
'''public void setAdditivity(final boolean additivity)
'''
pass
def setResourceBundle():
'''public void setResourceBundle(final ResourceBundle bundle)
'''
pass
def getResourceBundle():
'''public ResourceBundle getResourceBundle()
'''
pass
def assertLog():
'''public void assertLog(final boolean assertion, final String msg)
'''
pass
def l7dlog():
'''public void l7dlog(final Priority priority, final String key, final Throwable t)
public void l7dlog(final Priority priority, final String key, final Object[] params, final Throwable t)
'''
pass
def log():
'''public void log(final Priority priority, final Object message, final Throwable t)
public void log(final Priority priority, final Object message)
public void log(final String fqcn, final Priority priority, final Object message, final Throwable t)
'''
pass
def getContext():
'''public static LoggerContext getContext()
'''
pass
