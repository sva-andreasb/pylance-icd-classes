def ():
    '''returns MutableLogEvent\n\n
    ()\n
    (final StringBuilder msgText, final Object[] replacementParameters)\n
    '''
def toImmutable():
    '''returns Log4jLogEvent\n\n
    toImmutable()\n
    '''
def initFrom():
    '''returns None\n\n
    initFrom(final LogEvent event)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getLoggerFqcn():
    '''returns String\n\n
    getLoggerFqcn()\n
    '''
def setLoggerFqcn():
    '''returns None\n\n
    setLoggerFqcn(final String loggerFqcn)\n
    '''
def getMarker():
    '''returns Marker\n\n
    getMarker()\n
    '''
def setMarker():
    '''returns None\n\n
    setMarker(final Marker marker)\n
    '''
def getLevel():
    '''returns Level\n\n
    getLevel()\n
    '''
def setLevel():
    '''returns None\n\n
    setLevel(final Level level)\n
    '''
def getLoggerName():
    '''returns String\n\n
    getLoggerName()\n
    '''
def setLoggerName():
    '''returns None\n\n
    setLoggerName(final String loggerName)\n
    '''
def getMessage():
    '''returns Message\n\n
    getMessage()\n
    '''
def setMessage():
    '''returns None\n\n
    setMessage(final Message msg)\n
    '''
def getFormattedMessage():
    '''returns String\n\n
    getFormattedMessage()\n
    '''
def getFormat():
    '''returns String\n\n
    getFormat()\n
    '''
def getParameters():
    '''returns Object[]\n\n
    getParameters()\n
    '''
def getThrowable():
    '''returns Throwable\n\n
    getThrowable()\n
    '''
def formatTo():
    '''returns None\n\n
    formatTo(final StringBuilder buffer)\n
    '''
def swapParameters():
    '''returns Object[]\n\n
    swapParameters(final Object[] emptyReplacement)\n
    '''
def getParameterCount():
    '''returns short\n\n
    getParameterCount()\n
    '''
def memento():
    '''returns Message\n\n
    memento()\n
    '''
def getThrown():
    '''returns Throwable\n\n
    getThrown()\n
    '''
def setThrown():
    '''returns None\n\n
    setThrown(final Throwable thrown)\n
    '''
def getTimeMillis():
    '''returns long\n\n
    getTimeMillis()\n
    '''
def setTimeMillis():
    '''returns None\n\n
    setTimeMillis(final long timeMillis)\n
    '''
def getInstant():
    '''returns Instant\n\n
    getInstant()\n
    '''
def getThrownProxy():
    '''returns ThrowableProxy\n\n
    getThrownProxy()\n
    '''
def setSource():
    '''returns None\n\n
    setSource(final StackTraceElement source)\n
    '''
def getSource():
    '''returns StackTraceElement\n\n
    getSource()\n
    '''
def getContextData():
    '''returns ReadOnlyStringMap\n\n
    getContextData()\n
    '''
def setContextData():
    '''returns None\n\n
    setContextData(final StringMap mutableContextData)\n
    '''
def setContextStack():
    '''returns None\n\n
    setContextStack(final ThreadContext.ContextStack contextStack)\n
    '''
def getThreadId():
    '''returns long\n\n
    getThreadId()\n
    '''
def setThreadId():
    '''returns None\n\n
    setThreadId(final long threadId)\n
    '''
def getThreadName():
    '''returns String\n\n
    getThreadName()\n
    '''
def setThreadName():
    '''returns None\n\n
    setThreadName(final String threadName)\n
    '''
def getThreadPriority():
    '''returns int\n\n
    getThreadPriority()\n
    '''
def setThreadPriority():
    '''returns None\n\n
    setThreadPriority(final int threadPriority)\n
    '''
def isIncludeLocation():
    '''returns boolean\n\n
    isIncludeLocation()\n
    '''
def setIncludeLocation():
    '''returns None\n\n
    setIncludeLocation(final boolean includeLocation)\n
    '''
def isEndOfBatch():
    '''returns boolean\n\n
    isEndOfBatch()\n
    '''
def setEndOfBatch():
    '''returns None\n\n
    setEndOfBatch(final boolean endOfBatch)\n
    '''
def getNanoTime():
    '''returns long\n\n
    getNanoTime()\n
    '''
def setNanoTime():
    '''returns None\n\n
    setNanoTime(final long nanoTime)\n
    '''
def createMemento():
    '''returns Log4jLogEvent\n\n
    createMemento()\n
    '''
def initializeBuilder():
    '''returns None\n\n
    initializeBuilder(final Log4jLogEvent.Builder builder)\n
    '''
