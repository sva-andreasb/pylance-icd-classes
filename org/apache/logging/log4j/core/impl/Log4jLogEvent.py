def newBuilder():
    '''    public static Builder newBuilder()
    '''
def Log4jLogEvent():
    '''    public Log4jLogEvent()
    public Log4jLogEvent(final long timestamp)
    public Log4jLogEvent(final String loggerName, final Marker marker, final String loggerFQCN, final Level level, final Message message, final Throwable t)
    public Log4jLogEvent(final String loggerName, final Marker marker, final String loggerFQCN, final Level level, final Message message, final List<Property> properties, final Throwable t)
    public Log4jLogEvent(final String loggerName, final Marker marker, final String loggerFQCN, final StackTraceElement source, final Level level, final Message message, final List<Property> properties, final Throwable t)
    public Log4jLogEvent(final String loggerName, final Marker marker, final String loggerFQCN, final Level level, final Message message, final Throwable t, final Map<String, String> mdc, final ThreadContext.ContextStack ndc, final String threadName, final StackTraceElement location, final long timestampMillis)
    '''
def createEvent():
    '''    public static Log4jLogEvent createEvent(final String loggerName, final Marker marker, final String loggerFQCN, final Level level, final Message message, final Throwable thrown, final ThrowableProxy thrownProxy, final Map<String, String> mdc, final ThreadContext.ContextStack ndc, final String threadName, final StackTraceElement location, final long timestamp)
    '''
def getNanoClock():
    '''    public static NanoClock getNanoClock()
    '''
def setNanoClock():
    '''    public static void setNanoClock(final NanoClock nanoClock)
    '''
def asBuilder():
    '''    public Builder asBuilder()
    '''
def toImmutable():
    '''    public Log4jLogEvent toImmutable()
    '''
def getLevel():
    '''    public Level getLevel()
    '''
def getLoggerName():
    '''    public String getLoggerName()
    '''
def getMessage():
    '''    public Message getMessage()
    '''
def makeMessageImmutable():
    '''    public void makeMessageImmutable()
    '''
def getThreadId():
    '''    public long getThreadId()
    '''
def getThreadName():
    '''    public String getThreadName()
    '''
def getThreadPriority():
    '''    public int getThreadPriority()
    '''
def getTimeMillis():
    '''    public long getTimeMillis()
    '''
def getInstant():
    '''    public Instant getInstant()
    '''
def getThrown():
    '''    public Throwable getThrown()
    '''
def getThrownProxy():
    '''    public ThrowableProxy getThrownProxy()
    '''
def getMarker():
    '''    public Marker getMarker()
    '''
def getLoggerFqcn():
    '''    public String getLoggerFqcn()
    '''
def getContextData():
    '''    public ReadOnlyStringMap getContextData()
    '''
def getContextMap():
    '''    public Map<String, String> getContextMap()
    '''
def getSource():
    '''    public StackTraceElement getSource()
    '''
def isIncludeLocation():
    '''    public boolean isIncludeLocation()
    '''
def setIncludeLocation():
    '''    public void setIncludeLocation(final boolean includeLocation)
    public Builder setIncludeLocation(final boolean includeLocation)
    '''
def isEndOfBatch():
    '''    public boolean isEndOfBatch()
    '''
def setEndOfBatch():
    '''    public void setEndOfBatch(final boolean endOfBatch)
    public Builder setEndOfBatch(final boolean endOfBatch)
    '''
def getNanoTime():
    '''    public long getNanoTime()
    '''
def serialize():
    '''    public static Serializable serialize(final LogEvent event, final boolean includeLocation)
    public static Serializable serialize(final Log4jLogEvent event, final boolean includeLocation)
    '''
def canDeserialize():
    '''    public static boolean canDeserialize(final Serializable event)
    '''
def deserialize():
    '''    public static Log4jLogEvent deserialize(final Serializable event)
    '''
def createMemento():
    '''    public static LogEvent createMemento(final LogEvent logEvent)
    public static Log4jLogEvent createMemento(final LogEvent event, final boolean includeLocation)
    '''
def toString():
    '''    public String toString()
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def Builder():
    '''    public Builder()
    public Builder(final LogEvent other)
    '''
def setLevel():
    '''    public Builder setLevel(final Level level)
    '''
def setLoggerFqcn():
    '''    public Builder setLoggerFqcn(final String loggerFqcn)
    '''
def setLoggerName():
    '''    public Builder setLoggerName(final String loggerName)
    '''
def setMarker():
    '''    public Builder setMarker(final Marker marker)
    '''
def setMessage():
    '''    public Builder setMessage(final Message message)
    '''
def setThrown():
    '''    public Builder setThrown(final Throwable thrown)
    '''
def setTimeMillis():
    '''    public Builder setTimeMillis(final long timeMillis)
    '''
def setInstant():
    '''    public Builder setInstant(final Instant instant)
    '''
def setThrownProxy():
    '''    public Builder setThrownProxy(final ThrowableProxy thrownProxy)
    '''
def setContextMap():
    '''    public Builder setContextMap(final Map<String, String> contextMap)
    '''
def setContextData():
    '''    public Builder setContextData(final StringMap contextData)
    '''
def setContextStack():
    '''    public Builder setContextStack(final ThreadContext.ContextStack contextStack)
    '''
def setThreadId():
    '''    public Builder setThreadId(final long threadId)
    '''
def setThreadName():
    '''    public Builder setThreadName(final String threadName)
    '''
def setThreadPriority():
    '''    public Builder setThreadPriority(final int threadPriority)
    '''
def setSource():
    '''    public Builder setSource(final StackTraceElement source)
    '''
def setNanoTime():
    '''    public Builder setNanoTime(final long nanoTime)
    '''
def build():
    '''    public Log4jLogEvent build()
    '''
def LogEventProxy():
    '''    public LogEventProxy(final Log4jLogEvent event, final boolean includeLocation)
    public LogEventProxy(final LogEvent event, final boolean includeLocation)
    '''
