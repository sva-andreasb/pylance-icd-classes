def newBuilder():
'''public static Builder newBuilder()
'''
pass
def Log4jLogEvent():
'''public Log4jLogEvent()
public Log4jLogEvent(final long timestamp)
public Log4jLogEvent(final String loggerName, final Marker marker, final String loggerFQCN, final Level level, final Message message, final Throwable t)
public Log4jLogEvent(final String loggerName, final Marker marker, final String loggerFQCN, final Level level, final Message message, final List<Property> properties, final Throwable t)
public Log4jLogEvent(final String loggerName, final Marker marker, final String loggerFQCN, final StackTraceElement source, final Level level, final Message message, final List<Property> properties, final Throwable t)
public Log4jLogEvent(final String loggerName, final Marker marker, final String loggerFQCN, final Level level, final Message message, final Throwable t, final Map<String, String> mdc, final ThreadContext.ContextStack ndc, final String threadName, final StackTraceElement location, final long timestampMillis)
'''
pass
def createEvent():
'''public static Log4jLogEvent createEvent(final String loggerName, final Marker marker, final String loggerFQCN, final Level level, final Message message, final Throwable thrown, final ThrowableProxy thrownProxy, final Map<String, String> mdc, final ThreadContext.ContextStack ndc, final String threadName, final StackTraceElement location, final long timestamp)
'''
pass
def getNanoClock():
'''public static NanoClock getNanoClock()
'''
pass
def setNanoClock():
'''public static void setNanoClock(final NanoClock nanoClock)
'''
pass
def asBuilder():
'''public Builder asBuilder()
'''
pass
def toImmutable():
'''public Log4jLogEvent toImmutable()
'''
pass
def getLevel():
'''public Level getLevel()
'''
pass
def getLoggerName():
'''public String getLoggerName()
'''
pass
def getMessage():
'''public Message getMessage()
'''
pass
def makeMessageImmutable():
'''public void makeMessageImmutable()
'''
pass
def getThreadId():
'''public long getThreadId()
'''
pass
def getThreadName():
'''public String getThreadName()
'''
pass
def getThreadPriority():
'''public int getThreadPriority()
'''
pass
def getTimeMillis():
'''public long getTimeMillis()
'''
pass
def getInstant():
'''public Instant getInstant()
'''
pass
def getThrown():
'''public Throwable getThrown()
'''
pass
def getThrownProxy():
'''public ThrowableProxy getThrownProxy()
'''
pass
def getMarker():
'''public Marker getMarker()
'''
pass
def getLoggerFqcn():
'''public String getLoggerFqcn()
'''
pass
def getContextData():
'''public ReadOnlyStringMap getContextData()
'''
pass
def getContextMap():
'''public Map<String, String> getContextMap()
'''
pass
def getSource():
'''public StackTraceElement getSource()
'''
pass
def isIncludeLocation():
'''public boolean isIncludeLocation()
'''
pass
def setIncludeLocation():
'''public void setIncludeLocation(final boolean includeLocation)
public Builder setIncludeLocation(final boolean includeLocation)
'''
pass
def isEndOfBatch():
'''public boolean isEndOfBatch()
'''
pass
def setEndOfBatch():
'''public void setEndOfBatch(final boolean endOfBatch)
public Builder setEndOfBatch(final boolean endOfBatch)
'''
pass
def getNanoTime():
'''public long getNanoTime()
'''
pass
def serialize():
'''public static Serializable serialize(final LogEvent event, final boolean includeLocation)
public static Serializable serialize(final Log4jLogEvent event, final boolean includeLocation)
'''
pass
def canDeserialize():
'''public static boolean canDeserialize(final Serializable event)
'''
pass
def deserialize():
'''public static Log4jLogEvent deserialize(final Serializable event)
'''
pass
def createMemento():
'''public static LogEvent createMemento(final LogEvent logEvent)
public static Log4jLogEvent createMemento(final LogEvent event, final boolean includeLocation)
'''
pass
def toString():
'''public String toString()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def Builder():
'''public Builder()
public Builder(final LogEvent other)
'''
pass
def setLevel():
'''public Builder setLevel(final Level level)
'''
pass
def setLoggerFqcn():
'''public Builder setLoggerFqcn(final String loggerFqcn)
'''
pass
def setLoggerName():
'''public Builder setLoggerName(final String loggerName)
'''
pass
def setMarker():
'''public Builder setMarker(final Marker marker)
'''
pass
def setMessage():
'''public Builder setMessage(final Message message)
'''
pass
def setThrown():
'''public Builder setThrown(final Throwable thrown)
'''
pass
def setTimeMillis():
'''public Builder setTimeMillis(final long timeMillis)
'''
pass
def setInstant():
'''public Builder setInstant(final Instant instant)
'''
pass
def setThrownProxy():
'''public Builder setThrownProxy(final ThrowableProxy thrownProxy)
'''
pass
def setContextMap():
'''public Builder setContextMap(final Map<String, String> contextMap)
'''
pass
def setContextData():
'''public Builder setContextData(final StringMap contextData)
'''
pass
def setContextStack():
'''public Builder setContextStack(final ThreadContext.ContextStack contextStack)
'''
pass
def setThreadId():
'''public Builder setThreadId(final long threadId)
'''
pass
def setThreadName():
'''public Builder setThreadName(final String threadName)
'''
pass
def setThreadPriority():
'''public Builder setThreadPriority(final int threadPriority)
'''
pass
def setSource():
'''public Builder setSource(final StackTraceElement source)
'''
pass
def setNanoTime():
'''public Builder setNanoTime(final long nanoTime)
'''
pass
def build():
'''public Log4jLogEvent build()
'''
pass
def LogEventProxy():
'''public LogEventProxy(final Log4jLogEvent event, final boolean includeLocation)
public LogEventProxy(final LogEvent event, final boolean includeLocation)
'''
pass
