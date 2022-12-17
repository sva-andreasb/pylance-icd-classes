def ():
    '''returns LogEventProxy\n\n
    ()\n
    (final long timestamp)\n
    (final String loggerName, final Marker marker, final String loggerFQCN, final Level level, final Message message, final Throwable t)\n
    (final String loggerName, final Marker marker, final String loggerFQCN, final Level level, final Message message, final List<Property> properties, final Throwable t)\n
    (final String loggerName, final Marker marker, final String loggerFQCN, final StackTraceElement source, final Level level, final Message message, final List<Property> properties, final Throwable t)\n
    (final String loggerName, final Marker marker, final String loggerFQCN, final Level level, final Message message, final Throwable t, final Map<String, String> mdc, final ThreadContext.ContextStack ndc, final String threadName, final StackTraceElement location, final long timestampMillis)\n
    ()\n
    (final LogEvent other)\n
    (final Log4jLogEvent event, final boolean includeLocation)\n
    (final LogEvent event, final boolean includeLocation)\n
    '''
def asBuilder():
    '''returns Builder\n\n
    asBuilder()\n
    '''
def toImmutable():
    '''returns Log4jLogEvent\n\n
    toImmutable()\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel()\n
    '''
def getLoggerName():
    '''returns String\n\n
    getLoggerName()\n
    '''
def getMessage():
    '''returns Message\n\n
    getMessage()\n
    '''
def makeMessageImmutable():
    '''returns None\n\n
    makeMessageImmutable()\n
    '''
def getThreadId():
    '''returns long\n\n
    getThreadId()\n
    '''
def getThreadName():
    '''returns String\n\n
    getThreadName()\n
    '''
def getThreadPriority():
    '''returns int\n\n
    getThreadPriority()\n
    '''
def getTimeMillis():
    '''returns long\n\n
    getTimeMillis()\n
    '''
def getInstant():
    '''returns Instant\n\n
    getInstant()\n
    '''
def getThrown():
    '''returns Throwable\n\n
    getThrown()\n
    '''
def getThrownProxy():
    '''returns ThrowableProxy\n\n
    getThrownProxy()\n
    '''
def getMarker():
    '''returns Marker\n\n
    getMarker()\n
    '''
def getLoggerFqcn():
    '''returns String\n\n
    getLoggerFqcn()\n
    '''
def getContextData():
    '''returns ReadOnlyStringMap\n\n
    getContextData()\n
    '''
def getSource():
    '''returns StackTraceElement\n\n
    getSource()\n
    '''
def isIncludeLocation():
    '''returns boolean\n\n
    isIncludeLocation()\n
    '''
def setIncludeLocation():
    '''returns Builder\n\n
    setIncludeLocation(final boolean includeLocation)\n
    setIncludeLocation(final boolean includeLocation)\n
    '''
def isEndOfBatch():
    '''returns boolean\n\n
    isEndOfBatch()\n
    '''
def setEndOfBatch():
    '''returns Builder\n\n
    setEndOfBatch(final boolean endOfBatch)\n
    setEndOfBatch(final boolean endOfBatch)\n
    '''
def getNanoTime():
    '''returns long\n\n
    getNanoTime()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def setLevel():
    '''returns Builder\n\n
    setLevel(final Level level)\n
    '''
def setLoggerFqcn():
    '''returns Builder\n\n
    setLoggerFqcn(final String loggerFqcn)\n
    '''
def setLoggerName():
    '''returns Builder\n\n
    setLoggerName(final String loggerName)\n
    '''
def setMarker():
    '''returns Builder\n\n
    setMarker(final Marker marker)\n
    '''
def setMessage():
    '''returns Builder\n\n
    setMessage(final Message message)\n
    '''
def setThrown():
    '''returns Builder\n\n
    setThrown(final Throwable thrown)\n
    '''
def setTimeMillis():
    '''returns Builder\n\n
    setTimeMillis(final long timeMillis)\n
    '''
def setInstant():
    '''returns Builder\n\n
    setInstant(final Instant instant)\n
    '''
def setThrownProxy():
    '''returns Builder\n\n
    setThrownProxy(final ThrowableProxy thrownProxy)\n
    '''
def setContextMap():
    '''returns Builder\n\n
    setContextMap(final Map<String, String> contextMap)\n
    '''
def setContextData():
    '''returns Builder\n\n
    setContextData(final StringMap contextData)\n
    '''
def setContextStack():
    '''returns Builder\n\n
    setContextStack(final ThreadContext.ContextStack contextStack)\n
    '''
def setThreadId():
    '''returns Builder\n\n
    setThreadId(final long threadId)\n
    '''
def setThreadName():
    '''returns Builder\n\n
    setThreadName(final String threadName)\n
    '''
def setThreadPriority():
    '''returns Builder\n\n
    setThreadPriority(final int threadPriority)\n
    '''
def setSource():
    '''returns Builder\n\n
    setSource(final StackTraceElement source)\n
    '''
def setNanoTime():
    '''returns Builder\n\n
    setNanoTime(final long nanoTime)\n
    '''
def build():
    '''returns Log4jLogEvent\n\n
    build()\n
    '''
